"""
주문 관련 Pydantic 스키마
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal


class OrderRequest(BaseModel):
    """주문 파싱 요청"""
    order_text: str = Field(
        ..., 
        description="고객의 음성 주문 텍스트",
        example="치즈버거 세트 큰 거 하나랑 콜라 2개요"
    )


class OptionInfo(BaseModel):
    """옵션 정보"""
    option_id: Optional[int] = Field(None, description="옵션 ID")
    option_name: str = Field(..., description="옵션명")
    additional_price: float = Field(0.0, description="추가 가격")


class ParsedOrderItem(BaseModel):
    """파싱된 주문 항목"""
    product_id: int = Field(..., description="제품 ID")
    product_name: str = Field(..., description="제품명")
    quantity: int = Field(1, ge=1, description="수량")
    unit_price: float = Field(..., description="단가 (옵션 포함)")
    options: List[OptionInfo] = Field(default_factory=list, description="선택된 옵션 리스트")
    subtotal: float = Field(..., description="소계 (단가 × 수량)")


class ParsedOrderResponse(BaseModel):
    """주문 파싱 응답"""
    items: List[ParsedOrderItem] = Field(default_factory=list, description="파싱된 주문 항목 리스트")
    total_price: float = Field(0.0, description="총 금액")
    unrecognized_items: List[str] = Field(
        default_factory=list, 
        description="인식하지 못한 항목들"
    )
    confidence: float = Field(
        0.0, 
        ge=0.0, 
        le=1.0, 
        description="파싱 신뢰도 (0.0 ~ 1.0)"
    )
    notes: str = Field("", description="추가 메모 또는 특이사항")


class InitializeRAGResponse(BaseModel):
    """RAG 초기화 응답"""
    success: bool = Field(..., description="초기화 성공 여부")
    total_items: int = Field(..., description="임베딩된 메뉴 항목 수")
    message: str = Field(..., description="결과 메시지")


class HealthCheckResponse(BaseModel):
    """헬스체크 응답"""
    status: str = Field("healthy", description="서비스 상태")
    message: str = Field("Service is running", description="상태 메시지")


class ErrorResponse(BaseModel):
    """에러 응답"""
    error: str = Field(..., description="에러 메시지")
    detail: Optional[str] = Field(None, description="상세 에러 정보")


class MenuRecommendationRequest(BaseModel):
    """메뉴 추천 요청"""
    user_preference: str = Field(
        ...,
        description="사용자의 취향이나 요청사항",
        example="매운 거 좋아하고 오늘은 가볍게 먹고 싶어요"
    )
    max_results: Optional[int] = Field(
        5,
        ge=1,
        le=10,
        description="추천받을 메뉴 개수 (기본: 5개)"
    )


class RecommendedMenuItem(BaseModel):
    """추천된 메뉴 항목"""
    product_id: int = Field(..., description="제품 ID")
    product_name: str = Field(..., description="제품명")
    description: Optional[str] = Field(None, description="제품 설명")
    price: float = Field(..., description="가격")
    categories: str = Field(..., description="카테고리")
    recommendation_reason: str = Field(..., description="추천 이유")
    similarity_score: float = Field(..., description="유사도 점수")


class MenuRecommendationResponse(BaseModel):
    """메뉴 추천 응답"""
    recommendations: List[RecommendedMenuItem] = Field(
        default_factory=list,
        description="추천 메뉴 리스트"
    )
    user_preference: str = Field(..., description="사용자가 요청한 취향")
    total_count: int = Field(..., description="추천된 메뉴 개수")
    notes: str = Field("", description="추가 메모 또는 안내사항")
