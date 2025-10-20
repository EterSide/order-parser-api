"""
제품 Description 업데이트 스크립트
각 제품에 재료, 칼로리, 특징, 알레르기 정보 추가
"""
import csv
import json

def generate_detailed_description(product):
    """제품 타입에 따라 상세 description 생성"""
    product_id = product['product_id']
    product_name = product['product_name']
    original_desc = product['description']
    
    # 기본 설명 유지
    detailed_desc = original_desc
    
    # 제품 타입별 상세 정보 추가
    
    # 1. 음료 (물, 주스, 탄산음료, 커피 등)
    if any(keyword in product_name for keyword in ['미네랄워터', '순수']):
        detailed_desc = f"""{original_desc}
재료: 천연 미네랄워터
칼로리: 0kcal
특징: 무칼로리, 수분보충
알레르기: 없음"""
    
    elif '오렌지' in product_name:
        detailed_desc = f"""{original_desc}
재료: 오렌지 농축액, 비타민C
칼로리: 180kcal
특징: 비타민C 풍부, 상큼한 맛
알레르기: 없음"""
    
    elif '스프라이트' in product_name:
        if '제로' in product_name:
            size = 'L' if '(L)' in product_name else 'R'
            calories = '0kcal' if '제로' in product_name else ('250kcal' if size == 'L' else '180kcal')
            detailed_desc = f"""{original_desc}
재료: 탄산수, 라임향, 인공감미료
칼로리: {calories}
특징: 제로칼로리, 라임향, 청량감
알레르기: 없음"""
        else:
            size = 'L' if '(L)' in product_name else 'R'
            calories = '250kcal' if size == 'L' else '180kcal'
            detailed_desc = f"""{original_desc}
재료: 탄산수, 설탕, 라임향
칼로리: {calories}
특징: 라임향, 청량한 탄산음료
알레르기: 없음"""
    
    elif '코카콜라' in product_name:
        if '제로' in product_name:
            size = 'L' if '(L)' in product_name else 'R'
            detailed_desc = f"""{original_desc}
재료: 탄산수, 콜라향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 콜라맛, 다이어트
알레르기: 없음"""
        else:
            size = 'L' if '(L)' in product_name else 'R'
            calories = '280kcal' if size == 'L' else '200kcal'
            detailed_desc = f"""{original_desc}
재료: 탄산수, 설탕, 콜라향
칼로리: {calories}
특징: 클래식 콜라맛, 청량감
알레르기: 없음"""
    
    elif '닥터페퍼' in product_name or '닥더페퍼' in product_name:
        if '제로' in product_name:
            size = 'L' if '(L)' in product_name else 'R'
            detailed_desc = f"""{original_desc}
재료: 탄산수, 체리향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 체리맛, 독특한 향
알레르기: 없음"""
    
    elif '아메리카노' in product_name:
        if '아이스' in product_name:
            detailed_desc = f"""{original_desc}
재료: 에스프레소, 물, 얼음
칼로리: 5kcal
특징: 저칼로리, 커피향, 카페인, 시원함
알레르기: 없음"""
        else:
            detailed_desc = f"""{original_desc}
재료: 에스프레소, 뜨거운 물
칼로리: 5kcal
특징: 저칼로리, 커피향, 카페인, 따뜻함
알레르기: 없음"""
    
    elif '초코' in product_name and ('아이스' in product_name or '핫' in product_name):
        if '아이스' in product_name:
            detailed_desc = f"""{original_desc}
재료: 우유, 초콜릿 시럽, 얼음
칼로리: 350kcal
특징: 달콤함, 초콜릿맛, 시원함
알레르기: 우유"""
        else:
            detailed_desc = f"""{original_desc}
재료: 우유, 초콜릿 시럽
칼로리: 320kcal
특징: 달콤함, 초콜릿맛, 따뜻함
알레르기: 우유"""
    
    # 2. 디저트 (선데, 킹퓨전, 플로트)
    elif '선데' in product_name:
        if '초코' in product_name:
            detailed_desc = f"""{original_desc}
재료: 아이스크림, 초콜릿 시럽
칼로리: 380kcal
특징: 달콤함, 초콜릿맛, 디저트
알레르기: 우유, 대두"""
        elif '밀크' in product_name:
            detailed_desc = f"""{original_desc}
재료: 바닐라 아이스크림, 우유 시럽
칼로리: 320kcal
특징: 부드러움, 달콤함, 바닐라맛
알레르기: 우유, 대두"""
    
    elif '킹퓨전' in product_name:
        if '초코 브라우니' in product_name:
            detailed_desc = f"""{original_desc}
재료: 아이스크림, 초콜릿 브라우니, 초콜릿 시럽
칼로리: 520kcal
특징: 고칼로리, 달콤함, 초콜릿, 브라우니 식감
알레르기: 우유, 밀, 계란, 대두"""
        elif '카라멜' in product_name:
            detailed_desc = f"""{original_desc}
재료: 아이스크림, 버터쿠키, 카라멜 시럽
칼로리: 480kcal
특징: 고칼로리, 달콤함, 카라멜맛, 쿠키 식감
알레르기: 우유, 밀, 계란, 대두"""
    
    elif '킹플로트' in product_name:
        detailed_desc = f"""{original_desc}
재료: 닥터페퍼 제로, 바닐라 아이스크림
칼로리: 280kcal
특징: 탄산과 아이스크림의 조화, 달콤함
알레르기: 우유, 대두"""
    
    # 3. 소스 및 시즈닝
    elif '시즈닝' in product_name:
        if '매콤치즈' in product_name:
            detailed_desc = f"""{original_desc}
재료: 치즈 파우더, 칠리 파우더, 향신료
칼로리: 50kcal
특징: 매콤함, 치즈맛, 감자튀김용
알레르기: 우유"""
        elif '스윗어니언' in product_name:
            detailed_desc = f"""{original_desc}
재료: 양파 파우더, 설탕, 향신료
칼로리: 45kcal
특징: 달콤함, 양파맛, 감자튀김용
알레르기: 없음"""
        elif '구운갈릭' in product_name:
            detailed_desc = f"""{original_desc}
재료: 구운 마늘 파우더, 허브, 향신료
칼로리: 40kcal
특징: 마늘향, 고소함, 감자튀김용
알레르기: 없음"""
    
    elif '소스' in product_name:
        if '허니머스타드' in product_name:
            detailed_desc = f"""{original_desc}
재료: 꿀, 머스타드, 마요네즈
칼로리: 80kcal
특징: 달콤함, 새콤함, 디핑소스
알레르기: 계란, 대두"""
        elif '디아블로' in product_name:
            detailed_desc = f"""{original_desc}
재료: 칠리, 핫소스, 향신료
칼로리: 25kcal
특징: 매운맛, 불맛, 저칼로리
알레르기: 없음"""
        elif '스위트칠리' in product_name:
            detailed_desc = f"""{original_desc}
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음"""
    
    # 4. 사이드 (프라이, 너겟, 치즈스틱 등)
    elif '프렌치프라이' in product_name:
        size = 'L' if '(L)' in product_name else 'R'
        calories = '480kcal' if size == 'L' else '340kcal'
        detailed_desc = f"""{original_desc}
재료: 감자, 식물성 기름, 소금
칼로리: {calories}
특징: 바삭함, 짭짤함, 감자맛
알레르기: 없음"""
    
    elif '쉐이킹프라이' in product_name:
        if '매콤치즈' in product_name:
            detailed_desc = f"""{original_desc}
재료: 감자튀김, 매콤치즈 시즈닝
칼로리: 420kcal
특징: 바삭함, 매콤함, 치즈맛
알레르기: 우유"""
        elif '스윗어니언' in product_name:
            detailed_desc = f"""{original_desc}
재료: 감자튀김, 스윗어니언 시즈닝
칼로리: 410kcal
특징: 바삭함, 달콤함, 양파맛
알레르기: 없음"""
        elif '구운갈릭' in product_name:
            detailed_desc = f"""{original_desc}
재료: 감자튀김, 구운갈릭 시즈닝
칼로리: 400kcal
특징: 바삭함, 마늘향, 고소함
알레르기: 없음"""
    
    elif '트러플 프라이' in product_name:
        detailed_desc = f"""{original_desc}
재료: 감자튀김, 트러플 소스, 파마산 치즈
칼로리: 520kcal
특징: 고급 트러플향, 치즈맛, 고칼로리
알레르기: 우유"""
    
    elif '치즈스틱' in product_name:
        detailed_desc = f"""{original_desc}
재료: 21가지 치즈 블렌드, 빵가루
칼로리: 420kcal
특징: 쫄깃함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두"""
    
    elif '모짜볼' in product_name:
        pieces = '10조각' if '10' in product_name else '5조각'
        calories = '580kcal' if '10' in product_name else '290kcal'
        detailed_desc = f"""{original_desc}
재료: 모짜렐라 치즈, 빵가루
칼로리: {calories}
특징: 쫄깃함, 크리미함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두"""
    
    elif '코코넛슈림프' in product_name:
        if '9조각' in product_name:
            calories = 650
        elif '6조각' in product_name:
            calories = 430
        else:  # 3조각
            calories = 220
        detailed_desc = f"""{original_desc}
재료: 새우, 코코넛 빵가루, 스위트칠리소스
칼로리: {calories}kcal
특징: 바삭함, 코코넛향, 새우맛, 달콤한 소스
알레르기: 갑각류, 밀, 대두"""
    
    elif '바삭킹' in product_name:
        if '8조각' in product_name:
            calories = 620
        elif '4조각' in product_name:
            calories = 310
        else:  # 2조각
            calories = 155
        sauce = ''
        if '디아블로' in product_name:
            sauce = ', 디아블로소스 (매운맛)'
        elif '스위트칠리' in product_name:
            sauce = ', 스위트칠리소스 (달콤함)'
        detailed_desc = f"""{original_desc}
재료: 치킨{sauce}
칼로리: {calories}kcal
특징: 바삭함, 닭고기, 고단백{', 매운맛' if '디아블로' in product_name else ', 달콤함' if '스위트칠리' in product_name else ''}
알레르기: 밀, 대두, 계란"""
    
    elif '너겟킹' in product_name:
        if '10조각' in product_name:
            calories = 480
        elif '8조각' in product_name:
            calories = 380
        else:  # 4조각
            calories = 190
        detailed_desc = f"""{original_desc}
재료: 닭가슴살, 빵가루
칼로리: {calories}kcal
특징: 바삭함, 닭고기, 고단백, 순한맛
알레르기: 밀, 대두, 계란"""
    
    elif '어니언링' in product_name:
        size = 'L' if '(L)' in product_name else 'R'
        calories = '420kcal' if size == 'L' else '280kcal'
        detailed_desc = f"""{original_desc}
재료: 진짜 양파, 빵가루
칼로리: {calories}
특징: 바삭함, 양파맛, 고소함
알레르기: 밀, 대두"""
    
    elif '크리스피 텐더' in product_name:
        detailed_desc = f"""{original_desc}
재료: 닭안심, 크리스피 빵가루
칼로리: 380kcal
특징: 매우 바삭함, 닭고기, 고단백
알레르기: 밀, 대두, 계란"""
    
    elif '코울슬로' in product_name:
        detailed_desc = f"""{original_desc}
재료: 양배추, 당근, 마요네즈, 식초
칼로리: 150kcal
특징: 저칼로리, 신선함, 채소, 새콤달콤
알레르기: 계란, 대두"""
    
    elif '콘샐러드' in product_name:
        detailed_desc = f"""{original_desc}
재료: 옥수수, 마요네즈, 설탕
칼로리: 180kcal
특징: 저칼로리, 달콤함, 채소
알레르기: 계란, 대두"""
    
    # 5. 버거 (와퍼, 치킨버거 등)
    elif '와퍼' in product_name and '세트' not in product_name:
        # 단품 와퍼
        base_calories = 680
        ingredients = "불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파, 케첩, 마요네즈"
        features = "불맛, 소고기, 신선한 야채"
        
        if '불고기' in product_name:
            base_calories = 720
            ingredients = "불에 구운 소고기 패티, 불고기 소스, 양상추, 양파"
            features = "불맛, 소고기, 달콤한 불고기맛"
        elif '갈릭불고기' in product_name:
            base_calories = 740
            ingredients = "불에 구운 소고기 패티, 불고기 소스, 갈릭 소스, 양상추, 양파"
            features = "불맛, 소고기, 달콤함, 마늘향"
        elif '치즈' in product_name and '콰트로' not in product_name and '베이컨' not in product_name:
            base_calories = 730
            ingredients = "불에 구운 소고기 패티, 체다 치즈, 양상추, 토마토, 피클, 양파"
            features = "불맛, 소고기, 치즈맛"
        elif '베이컨치즈' in product_name:
            base_calories = 820
            ingredients = "불에 구운 소고기 패티, 베이컨, 체다 치즈, 양상추, 토마토"
            features = "불맛, 소고기, 베이컨, 치즈맛, 고칼로리"
        elif '콰트로치즈' in product_name:
            base_calories = 880
            ingredients = "불에 구운 소고기 패티, 4가지 치즈 (체다, 모짜렐라, 에멘탈, 파마산), 양상추"
            features = "불맛, 소고기, 진한 치즈맛, 고칼로리"
        elif '통새우' in product_name:
            base_calories = 760
            ingredients = "불에 구운 소고기 패티, 통새우, 양상추, 타르타르 소스"
            features = "불맛, 소고기, 새우, 해산물"
        elif '트러플 머쉬룸' in product_name:
            base_calories = 850
            ingredients = "불에 구운 소고기 패티, 트러플 소스, 머쉬룸, 치즈, 양상추"
            features = "불맛, 소고기, 고급 트러플향, 버섯, 고칼로리"
        elif '몬스터' in product_name:
            base_calories = 1200
            ingredients = "불에 구운 대용량 소고기 패티, 베이컨, 치즈, 양상추, 토마토"
            features = "불맛, 소고기, 대용량, 고칼로리, 배불리 먹기"
        
        if '주니어' in product_name:
            base_calories = int(base_calories * 0.6)  # 주니어는 60% 크기
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 밀, 계란, 우유, 대두, 토마토"""
    
    elif '세트' in product_name:
        # 세트 메뉴
        base_name = product_name.replace(' 세트', '').replace(' 라지세트', '')
        base_calories = 1100  # 버거 + 사이드 + 음료
        
        if '라지' in product_name:
            base_calories += 200  # 라지는 약 200kcal 더 높음
        
        side_drink = "프렌치프라이(R), 코카콜라(R)"
        if '라지' in product_name:
            side_drink = "프렌치프라이(L), 코카콜라(L)"
        
        detailed_desc = f"""{original_desc}
구성: 버거 + 사이드 + 음료
칼로리: 약 {base_calories}kcal (버거 포함)
특징: 세트 구성, {'라지 사이즈' if '라지' in product_name else '레귤러 사이즈'}, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토"""
    
    elif '치킨버거' in product_name and '세트' not in product_name:
        base_calories = 580
        ingredients = "바삭한 치킨 패티, 양상추, 마요네즈"
        features = "바삭함, 닭고기, 순한맛"
        
        if '치즈 마요' in product_name:
            base_calories = 650
            ingredients = "바삭한 치킨 패티, 치즈, 마요네즈, 양상추"
            features = "바삭함, 닭고기, 치즈맛, 순한맛"
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '치킨킹' in product_name and '세트' not in product_name:
        base_calories = 680
        ingredients = "킹 사이즈 치킨 패티, 양상추, 마요네즈"
        features = "대용량, 바삭함, 닭고기"
        
        if 'BLT' in product_name:
            base_calories = 780
            ingredients = "킹 사이즈 치킨 패티, 베이컨, 양상추, 토마토, 마요네즈"
            features = "대용량, 바삭함, 닭고기, 베이컨"
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '슈림프버거' in product_name and '세트' not in product_name:
        base_calories = 560
        ingredients = "바삭한 새우 패티, 양상추, 타르타르 소스"
        features = "바삭함, 새우, 해산물, 순한맛"
        
        if '통새우' in product_name:
            base_calories = 620
            ingredients = "바삭한 새우 패티, 통새우, 양상추, 타르타르 소스"
            features = "바삭함, 새우, 해산물, 통새우 식감"
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 갑각류, 밀, 계란, 대두"""
    
    elif '크리스퍼' in product_name and '세트' not in product_name:
        base_calories = 520
        ingredients = "바삭한 치킨, 양상추, 마요네즈, 토마토"
        features = "매우 바삭함, 닭고기, 순한맛"
        
        if 'BLT' in product_name:
            base_calories = 620
            ingredients = "바삭한 치킨, 베이컨, 양상추, 토마토, 마요네즈"
            features = "매우 바삭함, 닭고기, 베이컨, 야채"
        elif '치폴레' in product_name:
            base_calories = 580
            ingredients = "바삭한 치킨, 치폴레 소스, 양상추, 토마토"
            features = "매우 바삭함, 닭고기, 매운맛, 치폴레향"
        elif '마늘' in product_name:
            base_calories = 560
            ingredients = "바삭한 치킨, 마늘 소스, 양상추"
            features = "매우 바삭함, 닭고기, 마늘향"
        elif '랩' in product_name:
            base_calories = 480
            ingredients = "바삭한 치킨, 양상추, 마요네즈, 토르티야"
            features = "매우 바삭함, 닭고기, 가볍게 먹기, 한 손으로 먹기 편함"
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '비프불고기버거' in product_name and '세트' not in product_name:
        base_calories = 620
        ingredients = "소고기 패티, 불고기 소스, 양상추, 양파"
        features = "소고기, 달콤한 불고기맛"
        
        if '더블' in product_name:
            base_calories = 920
            ingredients = "더블 소고기 패티, 불고기 소스, 양상추, 양파"
            features = "소고기, 달콤한 불고기맛, 더블 패티, 고칼로리"
        
        detailed_desc = f"""{original_desc}
재료: {ingredients}
칼로리: {base_calories}kcal
특징: {features}
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '몬스터 주니어' in product_name and '세트' not in product_name:
        detailed_desc = f"""{original_desc}
재료: 대용량 소고기 패티, 베이컨, 치즈, 양상추, 토마토
칼로리: 850kcal
특징: 대용량, 소고기, 베이컨, 치즈맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토"""
    
    elif '치즈버거' in product_name and '와퍼' not in product_name and '세트' not in product_name:
        detailed_desc = f"""{original_desc}
재료: 소고기 패티, 체다 치즈, 양상추, 토마토, 피클
칼로리: 400kcal
특징: 소고기, 치즈맛, 기본 버거
알레르기: 밀, 계란, 우유, 대두, 토마토"""
    
    elif '오리지널스' in product_name and '세트' not in product_name:
        if '뉴욕 스테이크' in product_name:
            detailed_desc = f"""{original_desc}
재료: 뉴욕 스테이크, 양상추, 토마토, 특제 소스
칼로리: 820kcal
특징: 프리미엄, 스테이크, 고급 재료, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토"""
        elif '메이플 갈릭' in product_name:
            detailed_desc = f"""{original_desc}
재료: 소고기 패티, 메이플 갈릭 소스, 양상추, 베이컨
칼로리: 780kcal
특징: 프리미엄, 달콤함, 마늘향, 베이컨, 고칼로리
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '더오치 맥시멈' in product_name and '세트' not in product_name:
        detailed_desc = f"""{original_desc}
재료: 더블 소고기 패티, 특제 소스, 양상추, 토마토, 치즈
칼로리: 920kcal
특징: 프리미엄, 더블 패티, 특제 소스, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토"""
    
    elif '트러플 머쉬룸' in product_name and '세트' not in product_name:
        if '딥' in product_name:
            detailed_desc = f"""{original_desc}
재료: 더블 소고기 패티, 트러플 소스, 머쉬룸, 치즈
칼로리: 980kcal
특징: 고급 트러플향, 버섯, 더블 패티, 고칼로리
알레르기: 밀, 계란, 우유, 대두"""
        elif '핫' in product_name:
            detailed_desc = f"""{original_desc}
재료: 소고기 패티, 핫 트러플 소스, 머쉬룸, 치즈
칼로리: 850kcal
특징: 고급 트러플향, 버섯, 매운맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두"""
        elif '트리플' in product_name:
            detailed_desc = f"""{original_desc}
재료: 소고기 패티, 3가지 머쉬룸, 크림 소스, 치즈
칼로리: 820kcal
특징: 3가지 버섯, 크림맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두"""
    
    elif '트머와 팩' in product_name:
        detailed_desc = f"""{original_desc}
구성: 트러플 머쉬룸 와퍼 패키지 메뉴
칼로리: 약 1200kcal
특징: 트러플향, 버섯, 패키지 구성
알레르기: 밀, 계란, 우유, 대두"""
    
    return detailed_desc


def main():
    """메인 함수"""
    # CSV 파일 읽기
    csv_file = r'C:\Users\cjsau\OneDrive\바탕 화면\products.csv'
    
    products = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['product_id']:  # 빈 행 제외
                products.append(row)
    
    print(f"총 {len(products)}개 제품 발견\n")
    
    # SQL UPDATE 문 생성
    sql_updates = []
    
    for product in products:
        detailed_desc = generate_detailed_description(product)
        
        # SQL UPDATE 문 생성 (작은따옴표 이스케이프)
        escaped_desc = detailed_desc.replace("'", "''")
        
        sql_update = f"""UPDATE products 
SET description = '{escaped_desc}' 
WHERE product_id = {product['product_id']};"""
        
        sql_updates.append(sql_update)
    
    # SQL 파일 저장
    output_file = 'update_descriptions.sql'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("-- 제품 Description 업데이트 SQL\n")
        f.write("-- 재료, 칼로리, 특징, 알레르기 정보 추가\n\n")
        f.write('\n\n'.join(sql_updates))
    
    print(f"✅ SQL 파일 생성 완료: {output_file}")
    print(f"✅ {len(sql_updates)}개 UPDATE 문 생성")
    print("\n사용 방법:")
    print("1. MySQL/PostgreSQL에서 실행: source update_descriptions.sql")
    print("2. 또는 복사해서 직접 실행")
    print("\n샘플 (첫 3개):")
    for i, sql in enumerate(sql_updates[:3], 1):
        print(f"\n--- 제품 {i} ---")
        print(sql[:200] + "...")


if __name__ == "__main__":
    main()

