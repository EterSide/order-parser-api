"""
메뉴 추천 API 테스트 스크립트
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def print_section(title):
    """섹션 제목 출력"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def test_recommend_menus():
    """메뉴 추천 API 테스트"""
    
    # 테스트 케이스들
    test_cases = [
        {
            "user_preference": "매운 거 좋아해요. 불맛 나는 걸로 추천해주세요!",
            "max_results": 5
        },
        {
            "user_preference": "다이어트 중이라 가벼운 메뉴가 좋을 것 같아요",
            "max_results": 5
        },
        {
            "user_preference": "치즈 듬뿍 들어간 고칼로리 메뉴 좋아해요. 배불리 먹고 싶어요",
            "max_results": 5
        },
        {
            "user_preference": "어린이가 먹을 건데 매운 거 말고 순한 맛으로 추천해주세요",
            "max_results": 5
        },
        {
            "user_preference": "커피랑 디저트로 가볍게 먹고 싶어요",
            "max_results": 3
        },
        # 카테고리 특정 테스트 케이스 추가
        {
            "user_preference": "햄버거 추천해주세요. 소고기로 만든 것으로요",
            "max_results": 5
        },
        {
            "user_preference": "음료 뭐가 좋을까요? 제로칼로리로요",
            "max_results": 5
        },
        {
            "user_preference": "디저트 먹고 싶어요. 달콤한 걸로",
            "max_results": 3
        },
        {
            "user_preference": "사이드 메뉴 추천해주세요. 바삭한 걸로",
            "max_results": 5
        }
    ]
    
    for idx, test_case in enumerate(test_cases, 1):
        print_section(f"테스트 케이스 {idx}")
        print(f"📝 사용자 요청: {test_case['user_preference']}")
        print(f"🔢 추천 개수: {test_case['max_results']}개\n")
        
        try:
            # API 호출
            response = requests.post(
                f"{BASE_URL}/api/recommend-menus",
                json=test_case,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"✅ 추천 성공! (총 {result['total_count']}개 메뉴)")
                print()
                
                # 추천 메뉴 출력
                for i, menu in enumerate(result['recommendations'], 1):
                    print(f"{i}. 🍔 {menu['product_name']}")
                    print(f"   💰 가격: {menu['price']:,.0f}원")
                    print(f"   📂 카테고리: {menu['categories']}")
                    print(f"   ⭐ 유사도: {menu['similarity_score']:.2f}")
                    print(f"   💡 추천 이유:")
                    print(f"      {menu['recommendation_reason']}")
                    print()
                
                # 추가 안내사항
                if result.get('notes'):
                    print(f"📌 안내사항: {result['notes']}")
                
            else:
                print(f"❌ 오류 발생: {response.status_code}")
                print(response.text)
                
        except requests.exceptions.ConnectionError:
            print("❌ 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요.")
            print("   명령어: python main.py")
            return
        except Exception as e:
            print(f"❌ 예외 발생: {str(e)}")
        
        print()

def main():
    """메인 함수"""
    print("\n" + "🎉"*40)
    print("  메뉴 추천 API 테스트")
    print("🎉"*40)
    
    # 서버 상태 확인
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ 서버 연결 성공!")
        else:
            print("⚠️ 서버 응답이 정상적이지 않습니다.")
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다.")
        print("   서버를 먼저 실행해주세요: python main.py")
        return
    
    # 메뉴 추천 테스트
    test_recommend_menus()
    
    print_section("테스트 완료")
    print("✅ 모든 테스트가 완료되었습니다!")
    print("\n💡 팁: 다른 취향으로 직접 테스트해보세요!")
    print("   예시:")
    print('   curl -X POST "http://localhost:8000/api/recommend-menus" \\')
    print('        -H "Content-Type: application/json" \\')
    print('        -d \'{"user_preference": "매운 거 좋아해요", "max_results": 5}\'')
    print()

if __name__ == "__main__":
    main()

