"""
OpenAI GPT를 사용한 주문 텍스트 파싱 서비스
"""
from openai import OpenAI
from typing import List, Dict, Any, Optional
import json
import logging
from difflib import SequenceMatcher
from config import settings

logger = logging.getLogger(__name__)


class OrderParserService:
    """주문 파싱 서비스"""
    
    def __init__(self):
        """OpenAI 클라이언트 초기화"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
    
    def parse_order(
        self, 
        order_text: str, 
        similar_menus: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        주문 텍스트를 파싱하여 구조화된 주문 데이터로 변환
        
        Args:
            order_text: 고객의 주문 텍스트
            similar_menus: RAG로 검색된 유사 메뉴 리스트
            
        Returns:
            파싱된 주문 데이터
        """
        try:
            # 디버깅: 검색된 메뉴 목록 로깅
            logger.info(f"RAG 검색 결과 ({len(similar_menus)}개):")
            for idx, menu in enumerate(similar_menus[:5], 1):  # 상위 5개만
                logger.info(f"  {idx}. {menu['product_name']} (유사도: {menu.get('similarity_score', 0):.3f})")
            
            # 메뉴 컨텍스트 생성
            menu_context = self._build_menu_context(similar_menus)
            
            # 디버깅: GPT에게 전달되는 메뉴 컨텍스트 로깅
            logger.info("=" * 80)
            logger.info("GPT에게 전달되는 메뉴 컨텍스트:")
            logger.info(menu_context)
            logger.info("=" * 80)
            
            # 시스템 프롬프트
            system_prompt = """당신은 햄버거 가게 키오스크의 주문 파싱 전문가입니다.
고객의 음성 주문 텍스트를 받아서 정확한 메뉴와 수량, 옵션을 파악하여 JSON 형식으로 반환해야 합니다.

**핵심 원칙 (반드시 준수):**
⚠️ 주문 텍스트에 명시적으로 언급된 항목만 파싱하세요.
⚠️ 추론하거나 암시된 항목을 임의로 추가하지 마세요.
⚠️ 고객이 말하지 않은 메뉴는 절대 추가하지 마세요.

**파싱 지침:**
1. **제품 매칭:**
   - 제공된 메뉴 목록에서 주문 텍스트와 가장 유사한 제품을 찾으세요
   - 수량이 명시되지 않으면 1개로 간주
   - **"그냥", "기본", "일반", "오리지널" 등의 키워드가 있으면:**
     * 가장 기본형 제품을 선택하세요
     * 예: "그냥 와퍼" → "와퍼" (O), "콰트로치즈와퍼" (X)
     * 예: "기본 버거" → "버거" (O), "치즈버거" (X)
   - **제품명이 명확히 일치하지 않으면** unrecognized_items에 추가하세요
   
2. **세트 메뉴 처리 (매우 중요!):**
   - "세트"가 언급되면 세트 메뉴를 찾으세요
   - 세트 메뉴를 선택했다면, 사이드/음료는 반드시 해당 세트의 **옵션**에서 찾아야 합니다
   - "사이드는 XXX" → 세트의 사이드 옵션 그룹에서 XXX를 찾아서 options에 추가
   - "음료는 YYY" → 세트의 음료 옵션 그룹에서 YYY를 찾아서 options에 추가
   - 예시:
     * "사이드는 크리스퍼 랩" → 옵션 그룹 "사이드"에서 "크리스퍼 랩" 찾기
     * "음료는 코카콜라" → 옵션 그룹 "음료"에서 "코카콜라" 찾기
   - ⚠️ 사이드/음료를 별도의 제품으로 추가하지 마세요! 반드시 세트의 옵션으로 처리하세요!
   
3. **사이즈 처리:**
   - "라지", "L", "큰 거" → 라지 사이즈 옵션 또는 (L) 표시된 옵션
   - "레귤러", "R", "보통" → 레귤러 사이즈 옵션 또는 (R) 표시된 옵션
   - 사이즈가 음료/사이드에만 해당하는지, 제품 자체의 사이즈인지 문맥으로 판단

4. **음성 인식 오류 처리:**
   - 발음 유사성 고려 (예: "오렌즈" → "오렌지", "펩씨" → "펩시")
   - 띄어쓰기 무시 (예: "미닛메이드오렌지" = "미닛메이드 오렌지")
   - 철자 1-2개 차이 허용 (예: "크리스퍼" ≈ "크리스피")
   
5. **인식 실패 처리:**
   - 메뉴 목록에서 유사한 제품을 찾을 수 없으면 unrecognized_items에 추가

**응답 형식 (JSON):**
{
    "items": [
        {
            "product_id": 정수,
            "product_name": "제품명",
            "quantity": 정수,
            "unit_price": 실수,
            "options": [
                {
                    "option_id": 정수,
                    "option_name": "옵션명",
                    "additional_price": 실수
                }
            ],
            "subtotal": 실수
        }
    ],
    "total_price": 실수,
    "unrecognized_items": ["인식 못한 항목"],
    "confidence": 0.0~1.0,
    "notes": "특이사항 메모"
}"""
            
            # Few-shot 예제 (세트 메뉴 + 옵션 선택 + 기본형 선택)
            example_menu = """
1. 와퍼
   - Product ID: 50
   - 가격: 6000원

2. 치즈와퍼
   - Product ID: 51
   - 가격: 6500원

3. 불고기와퍼 세트
   - Product ID: 1
   - 가격: 8000원
   - 옵션 그룹:
     * 사이드: 프렌치프라이(R) (ID: 21), 어니언링(R) (ID: 22), 치즈스틱(R) (ID: 23)
     * 음료: 코카콜라(R) (ID: 31), 스프라이트(R) (ID: 32), 환타(R) (ID: 33)

4. 치즈스틱
   - Product ID: 20
   - 가격: 2500원
   
5. 코카콜라(R)
   - Product ID: 30
   - 가격: 2000원"""

            example_order = "불고기와퍼 세트 하나 주시고 사이드는 치즈스틱이고 음료는 환타로 주세요. 그리고 그냥 와퍼도 하나 추가해줘"
            
            example_response = """{
    "items": [
        {
            "product_id": 1,
            "product_name": "불고기와퍼 세트",
            "quantity": 1,
            "unit_price": 8000,
            "options": [
                {
                    "option_id": 23,
                    "option_name": "치즈스틱(R)",
                    "additional_price": 0
                },
                {
                    "option_id": 33,
                    "option_name": "환타(R)",
                    "additional_price": 0
                }
            ],
            "subtotal": 8000
        },
        {
            "product_id": 50,
            "product_name": "와퍼",
            "quantity": 1,
            "unit_price": 6000,
            "options": [],
            "subtotal": 6000
        }
    ],
    "total_price": 14000,
    "unrecognized_items": [],
    "confidence": 0.95,
    "notes": "세트 메뉴의 사이드를 치즈스틱, 음료를 환타로 선택. '그냥 와퍼'는 기본형 와퍼로 인식."
}"""
            
            # 사용자 프롬프트
            user_prompt = f"""**고객 주문:**
"{order_text}"

**사용 가능한 메뉴:**
{menu_context}

위 주문을 분석하여 JSON 형식으로 반환해주세요."""
            
            # OpenAI API 호출 (JSON mode with few-shot example)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"**고객 주문:**\n\"{example_order}\"\n\n**사용 가능한 메뉴:**\n{example_menu}\n\n위 주문을 분석하여 JSON 형식으로 반환해주세요."},
                    {"role": "assistant", "content": example_response},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.1,  # 일관성과 정확성을 위해 매우 낮은 temperature
                max_tokens=2000
            )
            
            # 응답 파싱
            result_text = response.choices[0].message.content
            parsed_result = json.loads(result_text)
            
            # 디버깅: GPT 응답 로깅
            logger.info("=" * 80)
            logger.info("GPT 응답:")
            logger.info(json.dumps(parsed_result, ensure_ascii=False, indent=2))
            logger.info("=" * 80)
            
            logger.info(f"주문 파싱 완료: {order_text} -> {len(parsed_result.get('items', []))}개 항목")
            
            return parsed_result
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 오류: {str(e)}")
            return self._create_error_response(f"응답 파싱 실패: {str(e)}")
        except Exception as e:
            logger.error(f"주문 파싱 중 오류: {str(e)}")
            return self._create_error_response(f"파싱 중 오류 발생: {str(e)}")
    
    def _build_menu_context(self, similar_menus: List[Dict[str, Any]]) -> str:
        """
        메뉴 정보를 LLM이 이해하기 쉬운 텍스트로 변환
        
        Args:
            similar_menus: 유사 메뉴 리스트
            
        Returns:
            포맷팅된 메뉴 컨텍스트 문자열
        """
        if not similar_menus:
            return "사용 가능한 메뉴가 없습니다."
        
        context_parts = []
        for idx, menu in enumerate(similar_menus, 1):
            menu_text = f"""
{idx}. {menu['product_name']} ({menu.get('product_eng_name', '')})
   - Product ID: {menu['product_id']}
   - 가격: {menu['price']}원
   - 카테고리: {menu['categories']}"""
            
            # 옵션 그룹 추가 (더 상세하게)
            if menu.get('option_groups'):
                menu_text += "\n   - 옵션 그룹:"
                for og in menu['option_groups']:
                    options_list = og.get('options', [])
                    if isinstance(options_list, list) and len(options_list) > 0:
                        # 옵션이 딕셔너리 형태인 경우 (option_id, option_name 포함)
                        if isinstance(options_list[0], dict):
                            options_str = ', '.join([f"{opt.get('option_name', '')} (ID: {opt.get('option_id', '')})" for opt in options_list])
                        else:
                            # 옵션이 문자열 리스트인 경우
                            options_str = ', '.join(options_list)
                        menu_text += f"\n     * {og['group_name']}: {options_str}"
            
            context_parts.append(menu_text)
        
        return "\n".join(context_parts)
    
    def _create_error_response(self, error_message: str) -> Dict[str, Any]:
        """
        오류 응답 생성
        
        Args:
            error_message: 오류 메시지
            
        Returns:
            오류 응답 딕셔너리
        """
        return {
            "items": [],
            "total_price": 0.0,
            "unrecognized_items": [],
            "confidence": 0.0,
            "notes": f"오류: {error_message}"
        }
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """
        두 문자열 간의 유사도 계산
        
        Args:
            str1: 비교할 첫 번째 문자열
            str2: 비교할 두 번째 문자열
            
        Returns:
            0.0~1.0 사이의 유사도 점수
        """
        # 소문자로 변환하고 공백 제거
        s1 = str1.lower().replace(" ", "")
        s2 = str2.lower().replace(" ", "")
        
        return SequenceMatcher(None, s1, s2).ratio()
    
    def _fuzzy_match_products(
        self, 
        query: str, 
        all_products: List[Dict[str, Any]], 
        threshold: float = 0.6
    ) -> Optional[Dict[str, Any]]:
        """
        Fuzzy matching으로 가장 유사한 제품 찾기
        
        Args:
            query: 검색할 제품명
            all_products: 모든 제품 정보
            threshold: 최소 유사도 임계값 (기본: 0.6)
            
        Returns:
            가장 유사한 제품 정보 (없으면 None)
        """
        best_match = None
        best_score = threshold
        
        for product in all_products:
            # 제품명과 비교
            score = self._calculate_similarity(query, product['product_name'])
            
            # 영문명이 있으면 영문명과도 비교
            if product.get('product_eng_name'):
                eng_score = self._calculate_similarity(query, product['product_eng_name'])
                score = max(score, eng_score)
            
            if score > best_score:
                best_score = score
                best_match = product
        
        if best_match:
            logger.info(f"Fuzzy match: '{query}' -> '{best_match['product_name']}' (유사도: {best_score:.2f})")
        
        return best_match
    
    def validate_parsed_order(
        self, 
        parsed_order: Dict[str, Any], 
        all_products: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        파싱된 주문의 유효성 검증 및 보정
        
        Args:
            parsed_order: 파싱된 주문 데이터
            all_products: 모든 제품 정보
            
        Returns:
            검증/보정된 주문 데이터
        """
        # 제품 ID 매핑
        product_map = {p['product_id']: p for p in all_products}
        
        validated_items = []
        total_price = 0.0
        
        for item in parsed_order.get('items', []):
            product_id = item.get('product_id')
            
            # 제품 존재 확인
            if product_id not in product_map:
                logger.warning(f"존재하지 않는 제품 ID: {product_id}")
                continue
            
            product = product_map[product_id]
            quantity = item.get('quantity', 1)
            
            # 기본 가격
            unit_price = product['price']
            
            # 옵션 가격 추가
            validated_options = []
            for option in item.get('options', []):
                # 옵션 유효성 검증 (실제로는 옵션 ID도 확인해야 함)
                validated_options.append({
                    "option_id": option.get('option_id'),
                    "option_name": option.get('option_name'),
                    "additional_price": option.get('additional_price', 0.0)
                })
                unit_price += option.get('additional_price', 0.0)
            
            subtotal = unit_price * quantity
            total_price += subtotal
            
            validated_items.append({
                "product_id": product_id,
                "product_name": product['product_name'],
                "quantity": quantity,
                "unit_price": unit_price,
                "options": validated_options,
                "subtotal": subtotal
            })
        
        # Fuzzy matching으로 unrecognized_items 재시도
        unrecognized_items = []
        fuzzy_matched_notes = []
        
        for unrecognized in parsed_order.get('unrecognized_items', []):
            matched_product = self._fuzzy_match_products(unrecognized, all_products, threshold=0.6)
            
            if matched_product:
                # 매칭된 제품을 items에 추가
                unit_price = matched_product['price']
                quantity = 1
                subtotal = unit_price * quantity
                total_price += subtotal
                
                validated_items.append({
                    "product_id": matched_product['product_id'],
                    "product_name": matched_product['product_name'],
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "options": [],
                    "subtotal": subtotal
                })
                
                fuzzy_matched_notes.append(f"'{unrecognized}' → '{matched_product['product_name']}'으로 자동 매칭")
                logger.info(f"Fuzzy matching 성공: {unrecognized} -> {matched_product['product_name']}")
            else:
                # 여전히 매칭 실패
                unrecognized_items.append(unrecognized)
                logger.warning(f"Fuzzy matching 실패: {unrecognized}")
        
        # Notes 업데이트
        notes = parsed_order.get('notes', '')
        if fuzzy_matched_notes:
            fuzzy_notes = " | ".join(fuzzy_matched_notes)
            notes = f"{notes} | {fuzzy_notes}" if notes else fuzzy_notes
        
        return {
            "items": validated_items,
            "total_price": total_price,
            "unrecognized_items": unrecognized_items,
            "confidence": parsed_order.get('confidence', 0.0),
            "notes": notes
        }


# 싱글톤 인스턴스
order_parser_service = OrderParserService()

