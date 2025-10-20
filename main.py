"""
FastAPI 메인 애플리케이션
LLM + RAG 기반 음성 주문 파싱 API
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import logging

from config import settings
from database.connection import get_db, init_db
from services.rag_service import rag_service
from services.order_parser import order_parser_service
from schemas.order_schema import (
    OrderRequest,
    ParsedOrderResponse,
    InitializeRAGResponse,
    HealthCheckResponse,
    ErrorResponse,
    MenuRecommendationRequest,
    MenuRecommendationResponse
)

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# FastAPI 앱 생성
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """애플리케이션 시작 시 실행"""
    logger.info("애플리케이션 시작 중...")
    # 데이터베이스 테이블 생성 (이미 존재하는 경우 무시)
    try:
        init_db()
        logger.info("데이터베이스 초기화 완료")
    except Exception as e:
        logger.error(f"데이터베이스 초기화 실패: {str(e)}")


@app.get("/", response_model=HealthCheckResponse)
async def root():
    """루트 엔드포인트"""
    return {
        "status": "healthy",
        "message": f"{settings.API_TITLE} v{settings.API_VERSION} is running"
    }


@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """헬스체크 엔드포인트"""
    return {
        "status": "healthy",
        "message": "Service is running"
    }


@app.post(
    "/api/initialize-rag",
    response_model=InitializeRAGResponse,
    summary="RAG 시스템 초기화",
    description="데이터베이스의 메뉴 데이터를 ChromaDB에 임베딩합니다."
)
async def initialize_rag(db: Session = Depends(get_db)):
    """
    RAG 시스템 초기화
    - 기존 ChromaDB 컬렉션 삭제
    - 데이터베이스에서 메뉴 데이터 로드
    - 메뉴 정보를 벡터 임베딩하여 ChromaDB에 저장
    """
    try:
        logger.info("RAG 시스템 초기화 시작")
        result = rag_service.initialize_collection(db)
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result["message"]
            )
        
        logger.info(f"RAG 초기화 완료: {result['total_items']}개 항목")
        return result
        
    except Exception as e:
        logger.error(f"RAG 초기화 오류: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"RAG 초기화 실패: {str(e)}"
        )


@app.post(
    "/api/parse-order",
    response_model=ParsedOrderResponse,
    summary="주문 텍스트 파싱",
    description="고객의 음성 주문 텍스트를 받아 구조화된 주문 데이터로 변환합니다."
)
async def parse_order(
    request: OrderRequest,
    db: Session = Depends(get_db)
):
    """
    주문 텍스트 파싱
    
    프로세스:
    1. RAG로 주문 텍스트와 유사한 메뉴 검색
    2. 검색된 메뉴 정보를 컨텍스트로 GPT에게 전달
    3. GPT가 주문을 파싱하여 구조화된 JSON 반환
    4. 결과 검증 및 보정
    
    Args:
        request: 주문 텍스트를 포함한 요청 객체
        db: 데이터베이스 세션
        
    Returns:
        파싱된 주문 데이터
    """
    try:
        logger.info(f"주문 파싱 요청: {request.order_text}")
        
        # 1. RAG로 유사 메뉴 검색 (하이브리드 검색)
        # 전체 주문 텍스트로 검색
        similar_menus_full = rag_service.search_similar_menus(
            query_text=request.order_text,
            top_k=settings.RAG_TOP_K
        )
        
        # 추가: 주요 키워드만 추출하여 재검색 (더 정확한 매칭)
        # 제품명만 추출: "세트", "버거", "선데" 등이 포함된 단어 추출
        import re
        keywords = []
        
        # 패턴 1: "XXX 세트" 형태 추출
        set_patterns = re.findall(r'(\S+\s*세트)', request.order_text)
        keywords.extend(set_patterns)
        
        # 패턴 2: "XXX 버거" 형태 추출
        burger_patterns = re.findall(r'(\S+\s*버거)', request.order_text)
        keywords.extend(burger_patterns)
        
        # 패턴 3: 기타 제품명 (선데, 프라이, 너겟 등)
        product_keywords = ['선데', '프라이', '너겟', '치킨', '콜라', '사이다', '주스', '커피', '와퍼', '버거']
        for keyword in product_keywords:
            if keyword in request.order_text:
                # 앞뒤 2단어 포함해서 추출
                match = re.search(rf'(\S+\s*\S*\s*{keyword}\s*\S*)', request.order_text)
                if match:
                    keywords.append(match.group(1).strip())
        
        # 패턴 4: 사이드/옵션 키워드 추출 ("사이드는 XXX", "음료는 XXX")
        option_patterns = [
            r'사이드[는은]?\s*(\S+(?:\s+\S+)?)',
            r'음료[는은]?\s*(\S+(?:\s+\S+)?)',
            r'디저트[는은]?\s*(\S+(?:\s+\S+)?)'
        ]
        for pattern in option_patterns:
            matches = re.findall(pattern, request.order_text)
            keywords.extend([m.strip() for m in matches])
        
        # 중복 제거 및 너무 긴 것 필터링 (20자 이내)
        keywords = list(set([k for k in keywords if len(k) <= 20]))
        
        # "그냥", "기본" 등의 수식어 제거 및 정확 매칭 플래그
        cleaned_keywords = []
        exact_match_keywords = []  # 정확히 일치해야 하는 키워드
        
        for keyword in keywords:
            # "그냥", "기본" 등이 있으면 정확 매칭 필요
            if re.match(r'^(그냥|기본|일반|오리지널)\s+', keyword):
                cleaned = re.sub(r'^(그냥|기본|일반|오리지널)\s+', '', keyword)
                exact_match_keywords.append(cleaned)
                logger.info(f"🎯 정확 매칭 필요: '{keyword}' → '{cleaned}'")
            else:
                cleaned = keyword
            cleaned_keywords.append(cleaned)
        
        keywords = list(set(cleaned_keywords))
        
        # 정확 매칭 키워드는 DB에서 정확히 일치하는 제품을 강제로 추가
        existing_ids = {m['product_id'] for m in similar_menus_full}
        
        for exact_keyword in exact_match_keywords:
            exact_results = rag_service.search_products_by_name(
                db=db,
                query=exact_keyword,
                threshold=0.95  # 95% 이상 일치만 (거의 정확히 일치)
            )
            # 정확히 일치하는 제품만 필터링
            for product in exact_results:
                if product['product_id'] in existing_ids:
                    continue  # 이미 있으면 스킵
                    
                product_name_lower = product['product_name'].lower().replace(" ", "")
                keyword_lower = exact_keyword.lower().replace(" ", "")
                # 정확히 일치하거나 매우 유사한 경우만
                if product_name_lower == keyword_lower:
                    product['similarity_score'] = 2.0  # 최고 우선순위
                    similar_menus_full.append(product)
                    existing_ids.add(product['product_id'])
                    logger.info(f"✅ 정확 매칭 추가: '{exact_keyword}' → '{product['product_name']}' (우선순위: 최고)")
                    break  # 첫 번째 정확 매칭만 사용
        
        # 각 키워드로 검색하여 결과 합치기
        similar_menus = similar_menus_full
        seen_ids = {m['product_id'] for m in similar_menus}
        
        for keyword in keywords[:5]:  # 상위 5개 키워드
            # RAG 검색
            keyword_results = rag_service.search_similar_menus(
                query_text=keyword,
                top_k=5  # 키워드당 5개씩
            )
            for menu in keyword_results:
                if menu['product_id'] not in seen_ids:
                    similar_menus.append(menu)
                    seen_ids.add(menu['product_id'])
            
            # Fallback: 직접 DB 검색 (RAG가 실패하는 경우 대비)
            db_results = rag_service.search_products_by_name(
                db=db,
                query=keyword,
                threshold=0.5  # 50% 이상 유사도
            )
            for menu in db_results[:3]:  # 상위 3개만
                if menu['product_id'] not in seen_ids:
                    similar_menus.append(menu)
                    seen_ids.add(menu['product_id'])
                    logger.info(f"📌 직접 DB 매칭 추가: {menu['product_name']} (키워드: {keyword})")
        
        # 정확 매칭 제품에 보너스 점수 부여 (시연용 개선)
        for menu in similar_menus:
            product_name_lower = menu['product_name'].lower().replace(" ", "")
            for keyword in keywords:
                keyword_lower = keyword.lower().replace(" ", "")
                # 정확히 일치하면 유사도를 1.5로 올림 (최우선 순위)
                if product_name_lower == keyword_lower:
                    menu['similarity_score'] = 1.5
                    logger.info(f"🎯 정확 매칭: '{keyword}' → '{menu['product_name']}'")
                    break
        
        # 유사도 순으로 정렬
        similar_menus = sorted(similar_menus, key=lambda x: x.get('similarity_score', 0), reverse=True)[:settings.RAG_TOP_K]
        
        # 디버깅: RAG 검색 결과 상세 로깅
        logger.info(f"=== 하이브리드 RAG 검색 결과 (TOP {len(similar_menus)}) ===")
        logger.info(f"키워드 추출: {keywords[:3]}")
        for idx, menu in enumerate(similar_menus[:10], 1):
            logger.info(f"{idx}. {menu['product_name']} (ID: {menu['product_id']}, 유사도: {menu.get('similarity_score', 0):.3f})")
        
        if not similar_menus:
            logger.warning("유사 메뉴를 찾을 수 없음")
            return ParsedOrderResponse(
                items=[],
                total_price=0.0,
                unrecognized_items=[request.order_text],
                confidence=0.0,
                notes="메뉴를 찾을 수 없습니다. RAG 시스템을 초기화해주세요."
            )
        
        logger.info(f"유사 메뉴 {len(similar_menus)}개 발견")
        
        # 2. GPT로 주문 파싱
        parsed_result = order_parser_service.parse_order(
            order_text=request.order_text,
            similar_menus=similar_menus
        )
        
        # 3. 결과 검증 및 보정
        all_products = rag_service.get_all_products(db)
        validated_result = order_parser_service.validate_parsed_order(
            parsed_order=parsed_result,
            all_products=all_products
        )
        
        logger.info(f"주문 파싱 완료: {len(validated_result['items'])}개 항목, 총 {validated_result['total_price']}원")
        
        return ParsedOrderResponse(**validated_result)
        
    except Exception as e:
        logger.error(f"주문 파싱 오류: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"주문 파싱 실패: {str(e)}"
        )


@app.get("/api/menus", summary="메뉴 목록 조회")
async def get_menus(db: Session = Depends(get_db)):
    """
    전체 메뉴 목록 조회 (테스트용)
    """
    try:
        menus = rag_service.get_all_products(db)
        return {
            "success": True,
            "total": len(menus),
            "menus": menus
        }
    except Exception as e:
        logger.error(f"메뉴 조회 오류: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"메뉴 조회 실패: {str(e)}"
        )


@app.post(
    "/api/recommend-menus",
    response_model=MenuRecommendationResponse,
    summary="메뉴 추천",
    description="사용자의 취향과 요청사항에 따라 적합한 메뉴를 추천합니다."
)
async def recommend_menus(
    request: MenuRecommendationRequest,
    db: Session = Depends(get_db)
):
    """
    메뉴 추천
    
    프로세스:
    1. 사용자의 취향/요청사항을 벡터 임베딩
    2. RAG로 유사한 메뉴 검색 (Vector DB)
    3. 검색된 메뉴 정보를 컨텍스트로 LLM에게 전달
    4. LLM이 사용자 취향에 맞는 메뉴를 선별하고 추천 이유 생성
    5. 추천 메뉴 리스트 반환
    
    Args:
        request: 사용자 취향/요청사항을 포함한 요청 객체
        db: 데이터베이스 세션
        
    Returns:
        추천 메뉴 리스트와 각 메뉴의 추천 이유
    """
    try:
        logger.info(f"메뉴 추천 요청: {request.user_preference}")
        
        # RAG + LLM을 사용한 메뉴 추천
        result = rag_service.recommend_menus(
            db=db,
            user_preference=request.user_preference,
            max_results=request.max_results or 5
        )
        
        logger.info(f"메뉴 추천 완료: {result['total_count']}개 메뉴 추천")
        
        return MenuRecommendationResponse(**result)
        
    except Exception as e:
        logger.error(f"메뉴 추천 오류: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"메뉴 추천 실패: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

