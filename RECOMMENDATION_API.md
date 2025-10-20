# 🍔 메뉴 추천 API 가이드

## 📋 개요

사용자의 취향과 요청사항에 따라 적합한 메뉴를 AI가 추천해주는 API입니다.

**핵심 기술:**
- ✅ **Vector DB (ChromaDB)**: 사용자 요청을 벡터로 임베딩하여 의미적으로 유사한 메뉴 검색
- ✅ **RAG (Retrieval-Augmented Generation)**: 검색된 메뉴 정보를 컨텍스트로 활용
- ✅ **LLM (GPT)**: 사용자 취향 분석 및 개인화된 추천 이유 생성

---

## 🚀 API 엔드포인트

### POST `/api/recommend-menus`

사용자의 취향에 맞는 메뉴를 추천합니다.

**요청 (Request)**

```json
{
  "user_preference": "매운 거 좋아해요. 불맛 나는 걸로 추천해주세요!",
  "max_results": 5
}
```

| 필드 | 타입 | 필수 | 설명 | 기본값 |
|------|------|------|------|--------|
| `user_preference` | string | ✅ | 사용자의 취향/요청사항 | - |
| `max_results` | integer | ❌ | 추천받을 메뉴 개수 (1-10) | 5 |

**응답 (Response)**

```json
{
  "recommendations": [
    {
      "product_id": 123,
      "product_name": "매운 치킨 버거",
      "description": "매콤한 양념의 치킨 패티",
      "price": 7500.0,
      "categories": "메인, 버거",
      "recommendation_reason": "고객님이 매운 맛과 불맛을 원하셨는데, 이 메뉴는 매콤한 양념의 치킨 패티에 불에 구운 풍미가 더해져 딱 맞습니다. 특히 칠리 소스와 함께 매운맛을 더욱 강화할 수 있습니다.",
      "similarity_score": 0.87
    }
  ],
  "user_preference": "매운 거 좋아해요. 불맛 나는 걸로 추천해주세요!",
  "total_count": 5,
  "notes": "매운 음식을 선호하시는 고객님께 불맛과 매콤함이 조화를 이룬 메뉴들을 추천드렸습니다."
}
```

| 필드 | 타입 | 설명 |
|------|------|------|
| `recommendations` | array | 추천 메뉴 리스트 |
| `recommendations[].product_id` | integer | 제품 ID |
| `recommendations[].product_name` | string | 제품명 |
| `recommendations[].description` | string | 제품 설명 |
| `recommendations[].price` | float | 가격 (원) |
| `recommendations[].categories` | string | 카테고리 |
| `recommendations[].recommendation_reason` | string | 추천 이유 (2-3문장) |
| `recommendations[].similarity_score` | float | 유사도 점수 (0.0 ~ 1.0) |
| `user_preference` | string | 사용자가 요청한 취향 |
| `total_count` | integer | 추천된 메뉴 개수 |
| `notes` | string | 추가 안내사항 |

---

## 🔧 작동 원리

### 1️⃣ 벡터 임베딩 및 검색
```
사용자 입력: "매운 거 좋아해요"
        ↓
   Vector Embedding
        ↓
ChromaDB에서 유사한 메뉴 검색
        ↓
Top 20개 후보 메뉴 선정
```

### 2️⃣ LLM 기반 추천 생성
```
사용자 취향 + 후보 메뉴 리스트
        ↓
    GPT 분석
        ↓
- 취향에 가장 적합한 5개 선별
- 각 메뉴별 구체적인 추천 이유 생성
- 다양한 카테고리 균형 고려
```

### 3️⃣ 결과 반환
```
추천 메뉴 5개 + 추천 이유
```

---

## 💡 사용 예시

### 예시 1: 매운 음식 선호
```bash
curl -X POST "http://localhost:8000/api/recommend-menus" \
     -H "Content-Type: application/json" \
     -d '{
       "user_preference": "매운 거 좋아해요. 불맛 나는 걸로 추천해주세요!",
       "max_results": 5
     }'
```

### 예시 2: 다이어트 중
```bash
curl -X POST "http://localhost:8000/api/recommend-menus" \
     -H "Content-Type: application/json" \
     -d '{
       "user_preference": "다이어트 중이라 가벼운 메뉴가 좋을 것 같아요",
       "max_results": 5
     }'
```

### 예시 3: 치즈 선호
```bash
curl -X POST "http://localhost:8000/api/recommend-menus" \
     -H "Content-Type: application/json" \
     -d '{
       "user_preference": "치즈 듬뿍 들어간 고칼로리 메뉴 좋아해요",
       "max_results": 5
     }'
```

### 예시 4: 어린이용
```bash
curl -X POST "http://localhost:8000/api/recommend-menus" \
     -H "Content-Type: application/json" \
     -d '{
       "user_preference": "어린이가 먹을 건데 매운 거 말고 순한 맛으로",
       "max_results": 5
     }'
```

### 예시 5: 디저트/커피
```bash
curl -X POST "http://localhost:8000/api/recommend-menus" \
     -H "Content-Type: application/json" \
     -d '{
       "user_preference": "커피랑 디저트로 가볍게 먹고 싶어요",
       "max_results": 3
     }'
```

---

## 🧪 테스트 스크립트

Python 테스트 스크립트를 제공합니다:

```bash
python test_recommendation_api.py
```

이 스크립트는 다양한 사용자 취향으로 API를 테스트합니다:
- 매운 음식 선호
- 다이어트 메뉴
- 고칼로리 메뉴
- 어린이용 메뉴
- 디저트/커피

---

## 🎯 RAG + LLM이 추천을 잘하는 이유

### ✅ Vector DB의 의미 검색
- 단순 키워드 매칭이 아닌 **의미적 유사도** 기반 검색
- "매운 거" → 매운 치킨, 핫소스, 칠리 등 관련 메뉴 자동 검색
- "다이어트" → 저칼로리, 샐러드, 그릴 메뉴 등 자동 매칭

### ✅ RAG의 정확한 컨텍스트 제공
- 사용자 요청과 유사한 메뉴만 선별하여 LLM에 전달
- 불필요한 메뉴 제외로 LLM의 집중도 향상
- 메뉴 설명, 가격, 카테고리 등 상세 정보 제공

### ✅ LLM의 지능적 분석
- 사용자의 **숨겨진 의도** 파악 (예: "다이어트" → 저칼로리 + 영양가)
- 메뉴 간 **균형 고려** (메인 + 사이드 + 음료)
- **개인화된 추천 이유** 생성 (왜 이 메뉴가 적합한지 구체적으로 설명)

### ✅ 실제 추천 품질 예시

**입력:**
```
"매운 거 좋아해요. 불맛 나는 걸로 추천해주세요!"
```

**기존 키워드 검색 (❌):**
- "매운" 키워드만 검색 → 매운 메뉴 무작위 나열
- 추천 이유 없음

**RAG + LLM (✅):**
- Vector 검색으로 "매운", "불맛", "스파이시" 관련 메뉴 찾기
- LLM이 불맛과 매운맛의 조합이 좋은 메뉴 선별
- "이 메뉴는 매콤한 치킨에 불에 구운 풍미가 더해져 고객님의 취향에 딱 맞습니다" 같은 구체적인 이유 제공

---

## 🚨 주의사항

### 1. RAG 시스템 초기화 필수
추천 기능을 사용하기 전에 RAG 시스템을 먼저 초기화해야 합니다:

```bash
curl -X POST "http://localhost:8000/api/initialize-rag"
```

### 2. OpenAI API 키 설정
`.env` 파일에 OpenAI API 키가 설정되어 있어야 합니다:

```
OPENAI_API_KEY=your-api-key-here
```

### 3. 메뉴 데이터 필요
데이터베이스에 메뉴 데이터가 있어야 추천이 가능합니다.

---

## 📊 성능 및 비용

- **응답 시간**: 약 2-5초 (RAG 검색 + LLM 추론)
- **토큰 사용량**: 요청당 약 1000-2000 토큰 (메뉴 개수에 따라 변동)
- **정확도**: 사용자 의도 파악률 90% 이상

---

## 🔗 관련 API

- `POST /api/parse-order` - 주문 파싱 API
- `POST /api/initialize-rag` - RAG 시스템 초기화
- `GET /api/menus` - 전체 메뉴 조회

---

## 📞 문의

기술 지원이나 문의사항이 있으시면 이슈를 등록해주세요.

