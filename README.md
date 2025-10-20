# LLM + RAG 음성 주문 파싱 API

햄버거 가게 음성인식 키오스크를 위한 주문 파싱 API입니다.
OpenAI GPT-4와 ChromaDB RAG를 활용하여 고객의 자연어 주문을 구조화된 데이터로 변환합니다.

## 주요 기능

- 🎯 **배치 처리**: 전체 주문 텍스트를 한 번에 처리하여 응답 속도 최적화
- 🔍 **RAG 기반 검색**: 벡터 임베딩을 통한 유사 메뉴 검색으로 정확도 향상
- 🤖 **GPT-4 파싱**: 자연어 이해 및 모호한 표현 처리
- 📊 **구조화된 출력**: 데이터베이스에 바로 저장 가능한 형식

## 기술 스택

- **FastAPI**: 비동기 웹 프레임워크
- **OpenAI GPT-4**: 자연어 처리
- **ChromaDB**: 벡터 데이터베이스 (RAG)
- **SQLAlchemy**: ORM
- **MySQL**: 관계형 데이터베이스

## 설치 방법

### 1. 의존성 설치

```bash
cd order-parser-api
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일 생성:

```bash
cp .env.example .env
```

`.env` 파일 수정:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/your_database
OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_MODEL=gpt-4-turbo-preview
CHROMA_PERSIST_DIR=./chroma_db
RAG_TOP_K=5
```

### 3. 데이터베이스 준비

MySQL 데이터베이스에 제품, 카테고리, 옵션 데이터가 있어야 합니다.

## 사용 방법

### 1. 서버 실행

```bash
python main.py
```

또는

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

서버가 http://localhost:8000 에서 실행됩니다.

### 2. RAG 시스템 초기화

처음 실행하거나 메뉴가 변경되었을 때 RAG 시스템을 초기화해야 합니다:

```bash
curl -X POST http://localhost:8000/api/initialize-rag
```

또는 Swagger UI에서: http://localhost:8000/docs

### 3. 주문 파싱 요청

```bash
curl -X POST http://localhost:8000/api/parse-order \
  -H "Content-Type: application/json" \
  -d '{"order_text": "치즈버거 세트 큰 거 하나랑 콜라 2개요"}'
```

**응답 예시:**

```json
{
  "items": [
    {
      "product_id": 1,
      "product_name": "치즈버거",
      "quantity": 1,
      "unit_price": 8500,
      "options": [
        {
          "option_id": 5,
          "option_name": "세트",
          "additional_price": 2000
        },
        {
          "option_id": 8,
          "option_name": "라지",
          "additional_price": 500
        }
      ],
      "subtotal": 11000
    },
    {
      "product_id": 10,
      "product_name": "콜라",
      "quantity": 2,
      "unit_price": 2000,
      "options": [],
      "subtotal": 4000
    }
  ],
  "total_price": 15000,
  "unrecognized_items": [],
  "confidence": 0.95,
  "notes": ""
}
```

## API 엔드포인트

### `GET /`
루트 엔드포인트 - 서비스 상태 확인

### `GET /health`
헬스체크 엔드포인트

### `POST /api/initialize-rag`
RAG 시스템 초기화 (메뉴 데이터를 ChromaDB에 임베딩)

### `POST /api/parse-order`
주문 텍스트 파싱

**Request Body:**
```json
{
  "order_text": "주문 내용"
}
```

**Response:**
```json
{
  "items": [...],
  "total_price": 0.0,
  "unrecognized_items": [],
  "confidence": 0.0,
  "notes": ""
}
```

### `GET /api/menus`
전체 메뉴 목록 조회 (테스트용)

## API 문서

서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 프로젝트 구조

```
order-parser-api/
├── main.py                 # FastAPI 앱 진입점
├── config.py              # 환경 설정
├── requirements.txt       # 의존성
├── .env                   # 환경 변수 (생성 필요)
├── .env.example          # 환경 변수 예시
├── README.md             # 프로젝트 문서
├── database/
│   ├── __init__.py
│   ├── connection.py     # MySQL 연결
│   └── models.py         # SQLAlchemy 모델
├── services/
│   ├── __init__.py
│   ├── rag_service.py    # ChromaDB RAG 로직
│   └── order_parser.py   # OpenAI GPT 주문 파싱
└── schemas/
    ├── __init__.py
    └── order_schema.py   # Pydantic 스키마
```

## 주의사항

1. **OpenAI API 키**: 반드시 유효한 OpenAI API 키가 필요합니다.
2. **데이터베이스 연결**: MySQL 데이터베이스가 실행 중이어야 합니다.
3. **RAG 초기화**: 첫 실행 시 반드시 `/api/initialize-rag`를 호출해야 합니다.
4. **메뉴 변경**: 메뉴가 변경될 때마다 RAG 재초기화가 필요합니다.

## 트러블슈팅

### ChromaDB 오류
```bash
rm -rf ./chroma_db
```
ChromaDB 디렉토리를 삭제하고 다시 초기화하세요.

### 데이터베이스 연결 오류
- MySQL 서버가 실행 중인지 확인
- `.env` 파일의 `DATABASE_URL` 확인
- 데이터베이스 사용자 권한 확인

### OpenAI API 오류
- API 키가 유효한지 확인
- API 사용 한도를 초과하지 않았는지 확인

## 라이선스

이 프로젝트는 교육 목적으로 제공됩니다.

