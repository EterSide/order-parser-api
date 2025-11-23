"""
환경 설정 관리
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # Database
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/kiosk_db"
    
    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    
    # ChromaDB
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    
    # API
    API_TITLE: str = "Order Parser API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "LLM + RAG 기반 음성 주문 파싱 API"
    
    # RAG
    RAG_TOP_K: int = 20  # 유사도 검색 결과 개수
    
    # Cache
    CACHE_TTL: int = 172800  # 캐시 TTL (48시간 = 48 * 3600초)
    CACHE_MAX_SIZE: int = 1000  # 최대 캐시 항목 개수
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 싱글톤 인스턴스
settings = Settings()

