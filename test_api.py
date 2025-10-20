"""
API 테스트 스크립트
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"


def print_response(title: str, response: requests.Response):
    """응답을 보기 좋게 출력"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except:
        print(response.text)


def test_health_check():
    """헬스체크 테스트"""
    response = requests.get(f"{BASE_URL}/health")
    print_response("헬스체크", response)
    return response.status_code == 200


def test_initialize_rag():
    """RAG 초기화 테스트"""
    response = requests.post(f"{BASE_URL}/api/initialize-rag")
    print_response("RAG 초기화", response)
    return response.status_code == 200


def test_parse_order(order_text: str):
    """주문 파싱 테스트"""
    data = {"order_text": order_text}
    response = requests.post(
        f"{BASE_URL}/api/parse-order",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    print_response(f"주문 파싱: '{order_text}'", response)
    return response.status_code == 200


def test_get_menus():
    """메뉴 목록 조회 테스트"""
    response = requests.get(f"{BASE_URL}/api/menus")
    print_response("메뉴 목록", response)
    return response.status_code == 200


def main():
    """테스트 메인 함수"""
    print("API 테스트 시작...")
    print(f"서버 URL: {BASE_URL}")
    
    # 1. 헬스체크
    if not test_health_check():
        print("\n❌ 서버가 실행되지 않았습니다. 먼저 서버를 시작하세요.")
        return
    
    print("\n✅ 서버가 정상적으로 실행 중입니다.")
    
    # 2. RAG 초기화
    print("\n\n🔄 RAG 시스템 초기화 중...")
    if test_initialize_rag():
        print("\n✅ RAG 초기화 완료")
    else:
        print("\n⚠️  RAG 초기화 실패 (데이터베이스 연결을 확인하세요)")
    
    # 3. 메뉴 목록 조회
    print("\n\n📋 메뉴 목록 조회 중...")
    test_get_menus()
    
    # 4. 주문 파싱 테스트
    print("\n\n🍔 주문 파싱 테스트 시작...")
    
    test_cases = [
        "치즈버거 세트 큰 거 하나요",
        "불고기버거 2개랑 콜라 라지 사이즈로 하나 주세요",
        "햄버거 하나, 감자튀김 큰 거, 콜라 2개",
        "빅맥 세트 2개 테이크아웃이요",
        "치킨버거요",
    ]
    
    for idx, test_case in enumerate(test_cases, 1):
        print(f"\n\n테스트 케이스 {idx}/{len(test_cases)}")
        test_parse_order(test_case)
    
    print("\n\n" + "="*60)
    print("  테스트 완료")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ 서버에 연결할 수 없습니다.")
        print("   먼저 서버를 시작하세요: python main.py")
    except KeyboardInterrupt:
        print("\n\n테스트 중단됨")
    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")

