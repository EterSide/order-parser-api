"""
RAG (Retrieval-Augmented Generation) 서비스
ChromaDB를 사용한 메뉴 검색
"""
import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils import embedding_functions
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from database.models import Product, Category, OptionGroup, Option, ProductCategory, ProductOptionGroup
from config import settings
import logging
from openai import OpenAI
import json

logger = logging.getLogger(__name__)


class RAGService:
    """RAG 서비스 클래스"""
    
    def __init__(self):
        """ChromaDB 클라이언트 및 OpenAI 클라이언트 초기화"""
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIR,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        
        # 한글 임베딩 함수 설정 (한국어 특화 모델)
        logger.info("한글 임베딩 모델 로딩 중: jhgan/ko-sroberta-multitask")
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="jhgan/ko-sroberta-multitask"
        )
        logger.info("한글 임베딩 모델 로딩 완료")
        
        self.collection_name = "menu_items"
        self.collection = None
        
        # OpenAI 클라이언트 초기화 (메뉴 추천용)
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
        
    def initialize_collection(self, db: Session) -> Dict[str, Any]:
        """
        ChromaDB 컬렉션 초기화 및 메뉴 데이터 임베딩
        
        Args:
            db: 데이터베이스 세션
            
        Returns:
            초기화 결과 정보
        """
        try:
            # 기존 컬렉션 삭제
            try:
                self.client.delete_collection(name=self.collection_name)
                logger.info(f"기존 컬렉션 '{self.collection_name}' 삭제 완료")
            except Exception:
                pass
            
            # 새 컬렉션 생성 (한글 임베딩 함수 적용)
            self.collection = self.client.create_collection(
                name=self.collection_name,
                embedding_function=self.embedding_function,
                metadata={"hnsw:space": "cosine"}  # 코사인 유사도 사용
            )
            logger.info(f"새 컬렉션 '{self.collection_name}' 생성 완료 (한글 임베딩 적용)")
            
            # 데이터베이스에서 메뉴 데이터 로드
            products = db.query(Product).filter(Product.is_available == True).all()
            
            documents = []
            metadatas = []
            ids = []
            
            for product in products:
                # 카테고리 정보 가져오기
                categories = [
                    pc.category.category_name 
                    for pc in product.product_categories
                ]
                
                # 옵션 그룹 정보 가져오기 (ID와 이름 포함)
                option_groups = []
                for pog in product.product_option_groups:
                    og = pog.option_group
                    options = [
                        {
                            "option_id": opt.option_id,
                            "option_name": opt.option_name,
                            "additional_price": float(opt.additional_price)
                        }
                        for opt in og.options
                    ]
                    option_groups.append({
                        "group_id": og.option_group_id,
                        "group_name": og.group_name,
                        "is_required": og.is_required,
                        "options": options
                    })
                
                # 검색용 문서 텍스트 생성 (한글 + 영문)
                # 옵션명 리스트 생성
                all_option_names = []
                for og in option_groups:
                    all_option_names.extend([opt['option_name'] for opt in og['options']])
                
                doc_text = f"""
                제품명: {product.product_name}
                영문명: {product.product_eng_name or ''}
                설명: {product.description or ''}
                카테고리: {', '.join(categories)}
                가격: {product.price}원
                옵션그룹: {', '.join([og['group_name'] for og in option_groups])}
                옵션: {', '.join(all_option_names)}
                """.strip()
                
                documents.append(doc_text)
                metadatas.append({
                    "product_id": str(product.product_id),
                    "product_name": product.product_name,
                    "product_eng_name": product.product_eng_name or "",
                    "price": str(product.price),
                    "categories": ", ".join(categories),
                    "option_groups": str(option_groups)
                })
                ids.append(f"product_{product.product_id}")
            
            # ChromaDB에 데이터 추가
            if documents:
                self.collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
                logger.info(f"{len(documents)}개의 메뉴 항목 임베딩 완료")
            
            return {
                "success": True,
                "total_items": len(documents),
                "message": f"{len(documents)}개의 메뉴 항목이 성공적으로 임베딩되었습니다."
            }
            
        except Exception as e:
            logger.error(f"컬렉션 초기화 중 오류: {str(e)}")
            return {
                "success": False,
                "total_items": 0,
                "message": f"초기화 중 오류 발생: {str(e)}"
            }
    
    def search_similar_menus(self, query_text: str, top_k: int = None) -> List[Dict[str, Any]]:
        """
        주문 텍스트와 유사한 메뉴 검색
        
        Args:
            query_text: 검색할 주문 텍스트
            top_k: 반환할 결과 개수 (기본값: settings.RAG_TOP_K)
            
        Returns:
            유사한 메뉴 항목 리스트
        """
        if top_k is None:
            top_k = settings.RAG_TOP_K
        
        try:
            # 컬렉션이 없으면 로드 (한글 임베딩 함수 적용)
            if self.collection is None:
                self.collection = self.client.get_collection(
                    name=self.collection_name,
                    embedding_function=self.embedding_function
                )
            
            # 유사도 검색
            results = self.collection.query(
                query_texts=[query_text],
                n_results=top_k
            )
            
            # 결과 포맷팅
            similar_menus = []
            if results and results['metadatas'] and results['metadatas'][0]:
                for metadata, distance in zip(
                    results['metadatas'][0], 
                    results['distances'][0]
                ):
                    similar_menus.append({
                        "product_id": int(metadata["product_id"]),
                        "product_name": metadata["product_name"],
                        "product_eng_name": metadata["product_eng_name"],
                        "price": float(metadata["price"]),
                        "categories": metadata["categories"],
                        "option_groups": eval(metadata["option_groups"]),  # 문자열을 다시 리스트로 변환
                        "similarity_score": 1 - distance  # 거리를 유사도로 변환
                    })
            
            logger.info(f"검색 완료: '{query_text}' -> {len(similar_menus)}개 결과")
            return similar_menus
            
        except Exception as e:
            logger.error(f"메뉴 검색 중 오류: {str(e)}")
            return []
    
    def search_products_by_name(self, db: Session, query: str, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """
        제품명으로 직접 검색 (Fallback용)
        
        Args:
            db: 데이터베이스 세션
            query: 검색할 제품명
            threshold: 최소 유사도 (기본: 0.3)
            
        Returns:
            매칭된 제품 정보 리스트
        """
        from difflib import SequenceMatcher
        
        products = db.query(Product).filter(Product.is_available == True).all()
        results = []
        
        query_lower = query.lower().replace(" ", "")
        
        for product in products:
            # 제품명 유사도 계산
            product_name_lower = product.product_name.lower().replace(" ", "")
            similarity = SequenceMatcher(None, query_lower, product_name_lower).ratio()
            
            # 영문명도 확인
            if product.product_eng_name:
                eng_name_lower = product.product_eng_name.lower().replace(" ", "")
                eng_similarity = SequenceMatcher(None, query_lower, eng_name_lower).ratio()
                similarity = max(similarity, eng_similarity)
            
            # 부분 매칭도 확인 (query가 product_name에 포함되는지)
            if query_lower in product_name_lower or product_name_lower in query_lower:
                similarity = max(similarity, 0.7)  # 부분 매칭은 최소 0.7점
            
            if similarity >= threshold:
                # 카테고리 정보
                categories = [pc.category.category_name for pc in product.product_categories]
                
                # 옵션 그룹 정보
                option_groups = []
                for pog in product.product_option_groups:
                    og = pog.option_group
                    options = [
                        {"option_id": opt.option_id, "option_name": opt.option_name, "additional_price": float(opt.additional_price)}
                        for opt in og.options
                    ]
                    option_groups.append({
                        "group_id": og.option_group_id,
                        "group_name": og.group_name,
                        "is_required": og.is_required,
                        "options": options
                    })
                
                results.append({
                    "product_id": product.product_id,
                    "product_name": product.product_name,
                    "product_eng_name": product.product_eng_name,
                    "description": product.description,
                    "price": float(product.price),
                    "categories": ", ".join(categories),
                    "option_groups": option_groups,
                    "similarity_score": similarity
                })
        
        # 유사도 순으로 정렬
        results.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        if results:
            logger.info(f"직접 DB 검색: '{query}' -> {len(results)}개 결과 (최고 유사도: {results[0]['similarity_score']:.3f})")
        
        return results
    
    def get_all_products(self, db: Session) -> List[Dict[str, Any]]:
        """
        모든 제품 정보 조회 (백업용)
        
        Args:
            db: 데이터베이스 세션
            
        Returns:
            모든 제품 정보 리스트
        """
        products = db.query(Product).filter(Product.is_available == True).all()
        
        result = []
        for product in products:
            categories = [pc.category.category_name for pc in product.product_categories]
            
            option_groups = []
            for pog in product.product_option_groups:
                og = pog.option_group
                options = [
                    {"option_id": opt.option_id, "option_name": opt.option_name, "additional_price": float(opt.additional_price)}
                    for opt in og.options
                ]
                option_groups.append({
                    "group_id": og.option_group_id,
                    "group_name": og.group_name,
                    "is_required": og.is_required,
                    "options": options
                })
            
            result.append({
                "product_id": product.product_id,
                "product_name": product.product_name,
                "product_eng_name": product.product_eng_name,
                "description": product.description,
                "price": float(product.price),
                "categories": categories,
                "option_groups": option_groups
            })
        
        return result
    
    def _extract_category_from_request(self, user_preference: str) -> str:
        """
        사용자 요청에서 카테고리 추출
        
        Args:
            user_preference: 사용자 요청사항
            
        Returns:
            추출된 카테고리 (버거, 음료, 디저트, 사이드, 전체)
        """
        preference_lower = user_preference.lower()
        
        # 카테고리 키워드 매칭
        category_keywords = {
            "버거": ["버거", "햄버거", "와퍼", "불고기", "치킨버거", "슈림프", "비프"],
            "음료": ["음료", "마실", "음료수", "콜라", "사이다", "커피", "아메리카노", "주스", "물", "제로"],
            "디저트": ["디저트", "후식", "달콤한", "아이스크림", "선데", "킹퓨전"],
            "사이드": ["사이드", "감자", "프라이", "너겟", "치킨", "어니언링", "치즈스틱", "샐러드"]
        }
        
        # 각 카테고리별로 키워드 매칭 점수 계산
        category_scores = {}
        for category, keywords in category_keywords.items():
            score = sum(1 for keyword in keywords if keyword in preference_lower)
            if score > 0:
                category_scores[category] = score
        
        # 가장 높은 점수의 카테고리 반환
        if category_scores:
            detected_category = max(category_scores, key=category_scores.get)
            logger.info(f"카테고리 감지: '{detected_category}' (키워드 매칭: {category_scores})")
            return detected_category
        
        return "전체"
    
    def _filter_by_category(self, menus: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
        """
        카테고리별로 메뉴 필터링
        
        Args:
            menus: 메뉴 리스트
            category: 카테고리 (버거, 음료, 디저트, 사이드)
            
        Returns:
            필터링된 메뉴 리스트
        """
        if category == "전체":
            return menus
        
        # 카테고리별 필터 조건
        category_filters = {
            "버거": lambda m: any(keyword in m['product_name'] for keyword in 
                ['버거', '와퍼', '크리스퍼', '치킨킹', '슈림프', '비프']),
            "음료": lambda m: any(keyword in m['categories'] for keyword in ['음료', '커피']) or
                            any(keyword in m['product_name'] for keyword in 
                ['콜라', '사이다', '스프라이트', '커피', '아메리카노', '주스', '물', '제로', '음료']),
            "디저트": lambda m: any(keyword in m['product_name'] for keyword in 
                ['선데', '킹퓨전', '플로트', '초코']),
            "사이드": lambda m: any(keyword in m['product_name'] for keyword in 
                ['프라이', '너겟', '어니언링', '치즈스틱', '모짜볼', '슈림프', '바삭킹', '샐러드', '코울슬로', '콘', '치즈스틱']) and
                            '버거' not in m['product_name'] and '세트' not in m['product_name']
        }
        
        filter_func = category_filters.get(category)
        if filter_func:
            filtered = [m for m in menus if filter_func(m)]
            logger.info(f"카테고리 '{category}' 필터링: {len(menus)}개 → {len(filtered)}개")
            return filtered if filtered else menus  # 필터 결과가 없으면 원본 반환
        
        return menus
    
    def recommend_menus(
        self, 
        db: Session, 
        user_preference: str, 
        max_results: int = 5
    ) -> Dict[str, Any]:
        """
        사용자 취향에 따른 메뉴 추천
        
        Args:
            db: 데이터베이스 세션
            user_preference: 사용자 취향/요청사항
            max_results: 추천할 메뉴 개수 (기본: 5)
            
        Returns:
            추천 메뉴 리스트 및 메타 정보
        """
        try:
            logger.info(f"메뉴 추천 요청: '{user_preference}'")
            
            # 0. 사용자 요청에서 카테고리 추출
            detected_category = self._extract_category_from_request(user_preference)
            
            # 1. RAG로 사용자 취향과 유사한 메뉴 검색
            # 검색 범위를 좀 더 넓게 (최대 30개로 증가 - 필터링 후 충분한 결과 보장)
            similar_menus = self.search_similar_menus(
                query_text=user_preference,
                top_k=30
            )
            
            if not similar_menus:
                logger.warning("유사 메뉴를 찾을 수 없음")
                return {
                    "recommendations": [],
                    "user_preference": user_preference,
                    "total_count": 0,
                    "notes": "추천할 메뉴를 찾을 수 없습니다. RAG 시스템을 초기화해주세요."
                }
            
            logger.info(f"RAG 검색 완료: {len(similar_menus)}개 후보 메뉴 발견")
            
            # 1.5. 카테고리 필터링 적용
            filtered_menus = self._filter_by_category(similar_menus, detected_category)
            
            if not filtered_menus:
                logger.warning(f"'{detected_category}' 카테고리 필터링 후 메뉴 없음, 원본 사용")
                filtered_menus = similar_menus
            
            # 2. 메뉴 컨텍스트 생성
            menu_context = self._build_recommendation_context(filtered_menus[:15])  # 상위 15개만 LLM에 전달
            
            # 3. LLM으로 추천 이유 생성
            # 카테고리 제약 조건 생성
            category_constraint = ""
            recommendation_principle_5 = "다양한 카테고리의 메뉴를 균형있게 추천하세요 (메인, 사이드, 음료 등)"
            
            if detected_category != "전체":
                category_map = {
                    "버거": "버거 메뉴만",
                    "음료": "음료 메뉴만",
                    "디저트": "디저트 메뉴만",
                    "사이드": "사이드 메뉴만"
                }
                category_constraint = f"\n⚠️ **중요**: 고객이 '{category_map.get(detected_category, detected_category)}' 요청했으므로, 반드시 해당 카테고리의 메뉴만 추천하세요!"
                recommendation_principle_5 = "해당 카테고리의 메뉴만 추천하세요"
            
            system_prompt = f"""당신은 햄버거 가게의 친절한 메뉴 추천 전문가입니다.
고객의 취향과 요청사항을 듣고, 가장 적합한 메뉴를 추천해주는 역할입니다.{category_constraint}

**추천 원칙:**
1. 고객의 취향과 요청사항을 정확히 파악하세요
2. 제공된 메뉴 목록에서 가장 적합한 메뉴를 선택하세요
3. 각 메뉴에 대해 **구체적이고 설득력 있는 추천 이유**를 작성하세요
4. 추천 이유는 고객의 요청사항과 메뉴의 특징을 연결해서 설명하세요
5. {recommendation_principle_5}

**추천 이유 작성 가이드:**
- "고객님이 [취향]을 원하셨는데, 이 메뉴는 [특징]이 있어 딱 맞습니다"
- 메뉴의 맛, 재료, 특징을 구체적으로 언급하세요
- 고객의 상황(다이어트, 매운 음식 선호 등)에 맞춰 설명하세요
- 친근하고 자연스러운 톤으로 작성하세요

**응답 형식 (JSON):**
{{
    "recommendations": [
        {{
            "product_id": 정수,
            "product_name": "제품명",
            "description": "제품 설명" (있으면),
            "price": 실수,
            "categories": "카테고리",
            "recommendation_reason": "구체적인 추천 이유 (2-3문장)",
            "similarity_score": 실수
        }}
    ],
    "notes": "전체적인 추천 안내사항 (선택사항)"
}}"""
            
            user_prompt = f"""**고객 취향/요청:**
"{user_preference}"

**추천 가능한 메뉴 목록:**
{menu_context}

위 고객의 취향에 가장 적합한 메뉴 **{max_results}개**를 선택하고, 각 메뉴마다 구체적인 추천 이유를 작성해주세요.
다양한 카테고리를 고려하여 균형있게 추천해주세요."""
            
            # OpenAI API 호출
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.7,  # 창의적인 추천 이유 생성을 위해 적당한 temperature
                max_tokens=2000
            )
            
            # 응답 파싱
            result_text = response.choices[0].message.content
            llm_result = json.loads(result_text)
            
            logger.info("=" * 80)
            logger.info("LLM 추천 결과:")
            logger.info(json.dumps(llm_result, ensure_ascii=False, indent=2))
            logger.info("=" * 80)
            
            # 4. 결과 포맷팅
            recommendations = llm_result.get('recommendations', [])
            
            return {
                "recommendations": recommendations,
                "user_preference": user_preference,
                "total_count": len(recommendations),
                "notes": llm_result.get('notes', '')
            }
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 오류: {str(e)}")
            return {
                "recommendations": [],
                "user_preference": user_preference,
                "total_count": 0,
                "notes": f"추천 생성 중 오류 발생: JSON 파싱 실패"
            }
        except Exception as e:
            logger.error(f"메뉴 추천 중 오류: {str(e)}")
            return {
                "recommendations": [],
                "user_preference": user_preference,
                "total_count": 0,
                "notes": f"추천 생성 중 오류 발생: {str(e)}"
            }
    
    def _build_recommendation_context(self, menus: List[Dict[str, Any]]) -> str:
        """
        추천용 메뉴 컨텍스트 생성
        
        Args:
            menus: 메뉴 리스트
            
        Returns:
            포맷팅된 메뉴 컨텍스트 문자열
        """
        if not menus:
            return "추천 가능한 메뉴가 없습니다."
        
        context_parts = []
        for idx, menu in enumerate(menus, 1):
            menu_text = f"""
{idx}. {menu['product_name']}
   - Product ID: {menu['product_id']}
   - 가격: {menu['price']}원
   - 카테고리: {menu['categories']}"""
            
            # 설명이 있으면 추가
            if menu.get('description'):
                menu_text += f"\n   - 설명: {menu['description']}"
            
            # 유사도 점수
            similarity = menu.get('similarity_score', 0)
            menu_text += f"\n   - 고객 취향과의 유사도: {similarity:.2f}"
            
            context_parts.append(menu_text)
        
        return "\n".join(context_parts)


# 싱글톤 인스턴스
rag_service = RAGService()

