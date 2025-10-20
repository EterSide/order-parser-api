-- 제품 Description 업데이트 SQL
-- 재료, 칼로리, 특징, 알레르기 정보 추가

UPDATE products 
SET description = '깨끗한 미네랄워터
재료: 천연 미네랄워터
칼로리: 0kcal
특징: 무칼로리, 수분보충
알레르기: 없음' 
WHERE product_id = 1;

UPDATE products 
SET description = '상큼한 오렌지 주스
재료: 오렌지 농축액, 비타민C
칼로리: 180kcal
특징: 비타민C 풍부, 상큼한 맛
알레르기: 없음' 
WHERE product_id = 2;

UPDATE products 
SET description = '칼로리 제로 라임맛 탄산음료 (L)
재료: 탄산수, 라임향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 라임향, 청량감
알레르기: 없음' 
WHERE product_id = 3;

UPDATE products 
SET description = '칼로리 제로 라임맛 탄산음료 (R)
재료: 탄산수, 라임향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 라임향, 청량감
알레르기: 없음' 
WHERE product_id = 4;

UPDATE products 
SET description = '라임맛 탄산음료 (L)
재료: 탄산수, 설탕, 라임향
칼로리: 250kcal
특징: 라임향, 청량한 탄산음료
알레르기: 없음' 
WHERE product_id = 5;

UPDATE products 
SET description = '라임맛 탄산음료 (R)
재료: 탄산수, 설탕, 라임향
칼로리: 180kcal
특징: 라임향, 청량한 탄산음료
알레르기: 없음' 
WHERE product_id = 6;

UPDATE products 
SET description = '칼로리 제로 체리맛 탄산음료 (R)
재료: 탄산수, 체리향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 체리맛, 독특한 향
알레르기: 없음' 
WHERE product_id = 7;

UPDATE products 
SET description = '칼로리 제로 체리맛 탄산음료 (L)
재료: 탄산수, 체리향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 체리맛, 독특한 향
알레르기: 없음' 
WHERE product_id = 8;

UPDATE products 
SET description = '시원한 아메리카노
재료: 에스프레소, 물, 얼음
칼로리: 5kcal
특징: 저칼로리, 커피향, 카페인, 시원함
알레르기: 없음' 
WHERE product_id = 9;

UPDATE products 
SET description = '따뜻한 핫초콜릿
재료: 우유, 초콜릿 시럽
칼로리: 320kcal
특징: 달콤함, 초콜릿맛, 따뜻함
알레르기: 우유' 
WHERE product_id = 10;

UPDATE products 
SET description = '따뜻한 아메리카노
재료: 에스프레소, 뜨거운 물
칼로리: 5kcal
특징: 저칼로리, 커피향, 카페인, 따뜻함
알레르기: 없음' 
WHERE product_id = 11;

UPDATE products 
SET description = '시원한 아이스초콜릿
재료: 우유, 초콜릿 시럽, 얼음
칼로리: 350kcal
특징: 달콤함, 초콜릿맛, 시원함
알레르기: 우유' 
WHERE product_id = 12;

UPDATE products 
SET description = '초콜릿 선데이
재료: 아이스크림, 초콜릿 시럽
칼로리: 380kcal
특징: 달콤함, 초콜릿맛, 디저트
알레르기: 우유, 대두' 
WHERE product_id = 13;

UPDATE products 
SET description = '초콜릿 브라우니 킹퓨전
재료: 아이스크림, 초콜릿 브라우니, 초콜릿 시럽
칼로리: 520kcal
특징: 고칼로리, 달콤함, 초콜릿, 브라우니 식감
알레르기: 우유, 밀, 계란, 대두' 
WHERE product_id = 14;

UPDATE products 
SET description = '닥터페퍼 제로 킹플로트
재료: 탄산수, 체리향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 체리맛, 독특한 향
알레르기: 없음' 
WHERE product_id = 15;

UPDATE products 
SET description = '시원한 코카콜라 (L)
재료: 탄산수, 설탕, 콜라향
칼로리: 280kcal
특징: 클래식 콜라맛, 청량감
알레르기: 없음' 
WHERE product_id = 16;

UPDATE products 
SET description = '시원한 코카콜라 (R)
재료: 탄산수, 설탕, 콜라향
칼로리: 200kcal
특징: 클래식 콜라맛, 청량감
알레르기: 없음' 
WHERE product_id = 17;

UPDATE products 
SET description = '칼로리 제로 코카콜라 (L)
재료: 탄산수, 콜라향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 콜라맛, 다이어트
알레르기: 없음' 
WHERE product_id = 18;

UPDATE products 
SET description = '칼로리 제로 코카콜라 (R)
재료: 탄산수, 콜라향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 콜라맛, 다이어트
알레르기: 없음' 
WHERE product_id = 19;

UPDATE products 
SET description = '부드러운 밀크 선데이
재료: 바닐라 아이스크림, 우유 시럽
칼로리: 320kcal
특징: 부드러움, 달콤함, 바닐라맛
알레르기: 우유, 대두' 
WHERE product_id = 20;

UPDATE products 
SET description = '카라멜 버터쿠키 킹퓨전
재료: 아이스크림, 버터쿠키, 카라멜 시럽
칼로리: 480kcal
특징: 고칼로리, 달콤함, 카라멜맛, 쿠키 식감
알레르기: 우유, 밀, 계란, 대두' 
WHERE product_id = 21;

UPDATE products 
SET description = '매콤한 치즈 시즈닝
재료: 치즈 파우더, 칠리 파우더, 향신료
칼로리: 50kcal
특징: 매콤함, 치즈맛, 감자튀김용
알레르기: 우유' 
WHERE product_id = 22;

UPDATE products 
SET description = '달콤한 어니언 시즈닝
재료: 양파 파우더, 설탕, 향신료
칼로리: 45kcal
특징: 달콤함, 양파맛, 감자튀김용
알레르기: 없음' 
WHERE product_id = 23;

UPDATE products 
SET description = '구운 마늘 시즈닝
재료: 구운 마늘 파우더, 허브, 향신료
칼로리: 40kcal
특징: 마늘향, 고소함, 감자튀김용
알레르기: 없음' 
WHERE product_id = 24;

UPDATE products 
SET description = '달콤한 허니머스타드 소스
재료: 꿀, 머스타드, 마요네즈
칼로리: 80kcal
특징: 달콤함, 새콤함, 디핑소스
알레르기: 계란, 대두' 
WHERE product_id = 25;

UPDATE products 
SET description = '매운 디아블로 소스
재료: 칠리, 핫소스, 향신료
칼로리: 25kcal
특징: 매운맛, 불맛, 저칼로리
알레르기: 없음' 
WHERE product_id = 26;

UPDATE products 
SET description = '달콤한 칠리 소스
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음' 
WHERE product_id = 27;

UPDATE products 
SET description = '신선한 코울슬로 샐러드
재료: 양배추, 당근, 마요네즈, 식초
칼로리: 150kcal
특징: 저칼로리, 신선함, 채소, 새콤달콤
알레르기: 계란, 대두' 
WHERE product_id = 28;

UPDATE products 
SET description = '달콤한 콘샐러드
재료: 옥수수, 마요네즈, 설탕
칼로리: 180kcal
특징: 저칼로리, 달콤함, 채소
알레르기: 계란, 대두' 
WHERE product_id = 29;

UPDATE products 
SET description = '바삭한 프렌치프라이 (L)
재료: 감자, 식물성 기름, 소금
칼로리: 480kcal
특징: 바삭함, 짭짤함, 감자맛
알레르기: 없음' 
WHERE product_id = 30;

UPDATE products 
SET description = '바삭한 프렌치프라이 (R)
재료: 감자, 식물성 기름, 소금
칼로리: 340kcal
특징: 바삭함, 짭짤함, 감자맛
알레르기: 없음' 
WHERE product_id = 31;

UPDATE products 
SET description = '매콤치즈 시즈닝 쉐이킹프라이
재료: 감자튀김, 매콤치즈 시즈닝
칼로리: 420kcal
특징: 바삭함, 매콤함, 치즈맛
알레르기: 우유' 
WHERE product_id = 32;

UPDATE products 
SET description = '스윗어니언 시즈닝 쉐이킹프라이
재료: 감자튀김, 스윗어니언 시즈닝
칼로리: 410kcal
특징: 바삭함, 달콤함, 양파맛
알레르기: 없음' 
WHERE product_id = 33;

UPDATE products 
SET description = '구운갈릭 시즈닝 쉐이킹프라이
재료: 감자튀김, 구운갈릭 시즈닝
칼로리: 400kcal
특징: 바삭함, 마늘향, 고소함
알레르기: 없음' 
WHERE product_id = 34;

UPDATE products 
SET description = '트러플 소스가 들어간 감자튀김
재료: 감자튀김, 트러플 소스, 파마산 치즈
칼로리: 520kcal
특징: 고급 트러플향, 치즈맛, 고칼로리
알레르기: 우유' 
WHERE product_id = 35;

UPDATE products 
SET description = '21가지 치즈가 들어간 치즈스틱
재료: 21가지 치즈 블렌드, 빵가루
칼로리: 420kcal
특징: 쫄깃함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두' 
WHERE product_id = 36;

UPDATE products 
SET description = '크리미한 모짜렐라 치즈볼 10조각
재료: 모짜렐라 치즈, 빵가루
칼로리: 580kcal
특징: 쫄깃함, 크리미함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두' 
WHERE product_id = 37;

UPDATE products 
SET description = '크리미한 모짜렐라 치즈볼 5조각
재료: 모짜렐라 치즈, 빵가루
칼로리: 290kcal
특징: 쫄깃함, 크리미함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두' 
WHERE product_id = 38;

UPDATE products 
SET description = '코코넛 튀김 새우 6조각 + 스위트칠리소스
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음' 
WHERE product_id = 39;

UPDATE products 
SET description = '코코넛 튀김 새우 9조각 + 스위트칠리소스
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음' 
WHERE product_id = 40;

UPDATE products 
SET description = '코코넛 튀김 새우 3조각 + 스위트칠리소스
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음' 
WHERE product_id = 41;

UPDATE products 
SET description = '바삭한 치킨 8조각 + 스위트칠리소스
재료: 칠리, 설탕, 식초
칼로리: 60kcal
특징: 달콤함, 약간 매운맛
알레르기: 없음' 
WHERE product_id = 42;

UPDATE products 
SET description = '바삭한 치킨 8조각 + 디아블로소스
재료: 칠리, 핫소스, 향신료
칼로리: 25kcal
특징: 매운맛, 불맛, 저칼로리
알레르기: 없음' 
WHERE product_id = 43;

UPDATE products 
SET description = '바삭한 치킨너겟 10조각
재료: 닭가슴살, 빵가루
칼로리: 480kcal
특징: 바삭함, 닭고기, 고단백, 순한맛
알레르기: 밀, 대두, 계란' 
WHERE product_id = 44;

UPDATE products 
SET description = '바삭한 치킨너겟 8조각
재료: 닭가슴살, 빵가루
칼로리: 380kcal
특징: 바삭함, 닭고기, 고단백, 순한맛
알레르기: 밀, 대두, 계란' 
WHERE product_id = 45;

UPDATE products 
SET description = '진짜 양파로 만든 어니언링 (L)
재료: 진짜 양파, 빵가루
칼로리: 420kcal
특징: 바삭함, 양파맛, 고소함
알레르기: 밀, 대두' 
WHERE product_id = 46;

UPDATE products 
SET description = '바삭한 치킨 4조각
재료: 치킨
칼로리: 310kcal
특징: 바삭함, 닭고기, 고단백
알레르기: 밀, 대두, 계란' 
WHERE product_id = 47;

UPDATE products 
SET description = '바삭한 치킨너겟 4조각
재료: 닭가슴살, 빵가루
칼로리: 190kcal
특징: 바삭함, 닭고기, 고단백, 순한맛
알레르기: 밀, 대두, 계란' 
WHERE product_id = 48;

UPDATE products 
SET description = '진짜 양파로 만든 어니언링 (R)
재료: 진짜 양파, 빵가루
칼로리: 280kcal
특징: 바삭함, 양파맛, 고소함
알레르기: 밀, 대두' 
WHERE product_id = 49;

UPDATE products 
SET description = '바삭한 치킨 2조각
재료: 치킨
칼로리: 155kcal
특징: 바삭함, 닭고기, 고단백
알레르기: 밀, 대두, 계란' 
WHERE product_id = 50;

UPDATE products 
SET description = '바삭한 크리스피 텐더
재료: 닭안심, 크리스피 빵가루
칼로리: 380kcal
특징: 매우 바삭함, 닭고기, 고단백
알레르기: 밀, 대두, 계란' 
WHERE product_id = 51;

UPDATE products 
SET description = '클래식 와퍼
재료: 불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파, 케첩, 마요네즈
칼로리: 680kcal
특징: 불맛, 소고기, 신선한 야채
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 52;

UPDATE products 
SET description = '와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 53;

UPDATE products 
SET description = '와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 54;

UPDATE products 
SET description = '달콤한 불고기 소스의 와퍼
재료: 불에 구운 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 720kcal
특징: 불맛, 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 55;

UPDATE products 
SET description = '불고기와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 56;

UPDATE products 
SET description = '불고기와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 57;

UPDATE products 
SET description = '갈릭 소스가 들어간 불고기와퍼
재료: 불에 구운 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 720kcal
특징: 불맛, 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 58;

UPDATE products 
SET description = '갈릭불고기와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 59;

UPDATE products 
SET description = '갈릭불고기와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 60;

UPDATE products 
SET description = '치즈가 들어간 와퍼
재료: 불에 구운 소고기 패티, 체다 치즈, 양상추, 토마토, 피클, 양파
칼로리: 730kcal
특징: 불맛, 소고기, 치즈맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 61;

UPDATE products 
SET description = '치즈와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 62;

UPDATE products 
SET description = '치즈와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 63;

UPDATE products 
SET description = '베이컨과 치즈가 들어간 와퍼
재료: 불에 구운 소고기 패티, 베이컨, 체다 치즈, 양상추, 토마토
칼로리: 820kcal
특징: 불맛, 소고기, 베이컨, 치즈맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 64;

UPDATE products 
SET description = '베이컨치즈와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 65;

UPDATE products 
SET description = '베이컨치즈와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 66;

UPDATE products 
SET description = '4가지 치즈가 들어간 와퍼
재료: 불에 구운 소고기 패티, 4가지 치즈 (체다, 모짜렐라, 에멘탈, 파마산), 양상추
칼로리: 880kcal
특징: 불맛, 소고기, 진한 치즈맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 67;

UPDATE products 
SET description = '콰트로치즈와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 68;

UPDATE products 
SET description = '콰트로치즈와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 69;

UPDATE products 
SET description = '통새우가 들어간 와퍼
재료: 불에 구운 소고기 패티, 통새우, 양상추, 타르타르 소스
칼로리: 760kcal
특징: 불맛, 소고기, 새우, 해산물
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 70;

UPDATE products 
SET description = '통새우와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 71;

UPDATE products 
SET description = '통새우와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 72;

UPDATE products 
SET description = '트러플 소스와 머쉬룸이 들어간 와퍼
재료: 불에 구운 소고기 패티, 트러플 소스, 머쉬룸, 치즈, 양상추
칼로리: 850kcal
특징: 불맛, 소고기, 고급 트러플향, 버섯, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 73;

UPDATE products 
SET description = '트러플 머쉬룸 와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 74;

UPDATE products 
SET description = '트러플 머쉬룸 와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 75;

UPDATE products 
SET description = '대용량 몬스터와퍼
재료: 불에 구운 대용량 소고기 패티, 베이컨, 치즈, 양상추, 토마토
칼로리: 1200kcal
특징: 불맛, 소고기, 대용량, 고칼로리, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 76;

UPDATE products 
SET description = '몬스터와퍼 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 77;

UPDATE products 
SET description = '몬스터와퍼 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 78;

UPDATE products 
SET description = '기본 와퍼 주니어
재료: 불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파, 케첩, 마요네즈
칼로리: 408kcal
특징: 불맛, 소고기, 신선한 야채
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 79;

UPDATE products 
SET description = '와퍼주니어 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 80;

UPDATE products 
SET description = '와퍼주니어 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 81;

UPDATE products 
SET description = '불고기 소스의 와퍼 주니어
재료: 불에 구운 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 432kcal
특징: 불맛, 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 82;

UPDATE products 
SET description = '불고기와퍼주니어 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 83;

UPDATE products 
SET description = '불고기와퍼주니어 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 84;

UPDATE products 
SET description = '치즈가 들어간 와퍼 주니어
재료: 불에 구운 소고기 패티, 체다 치즈, 양상추, 토마토, 피클, 양파
칼로리: 438kcal
특징: 불맛, 소고기, 치즈맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 85;

UPDATE products 
SET description = '치즈와퍼주니어 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 86;

UPDATE products 
SET description = '통새우가 들어간 와퍼 주니어
재료: 불에 구운 소고기 패티, 통새우, 양상추, 타르타르 소스
칼로리: 456kcal
특징: 불맛, 소고기, 새우, 해산물
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 87;

UPDATE products 
SET description = '통새우와퍼주니어 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 88;

UPDATE products 
SET description = '통새우와퍼주니어 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 89;

UPDATE products 
SET description = '4가지 치즈가 들어간 와퍼 주니어
재료: 불에 구운 소고기 패티, 4가지 치즈 (체다, 모짜렐라, 에멘탈, 파마산), 양상추
칼로리: 528kcal
특징: 불맛, 소고기, 진한 치즈맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 90;

UPDATE products 
SET description = '콰트로치즈와퍼주니어 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 91;

UPDATE products 
SET description = '콰트로치즈와퍼주니어 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 92;

UPDATE products 
SET description = '달콤한 불고기 소스의 비프버거
재료: 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 620kcal
특징: 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 93;

UPDATE products 
SET description = '비프불고기버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 94;

UPDATE products 
SET description = '비프불고기버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 95;

UPDATE products 
SET description = '더블 패티 비프불고기버거
재료: 더블 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 920kcal
특징: 소고기, 달콤한 불고기맛, 더블 패티, 고칼로리
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 96;

UPDATE products 
SET description = '더블비프불고기버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 97;

UPDATE products 
SET description = '더블비프불고기버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 98;

UPDATE products 
SET description = '대용량 몬스터 주니어버거
재료: 대용량 소고기 패티, 베이컨, 치즈, 양상추, 토마토
칼로리: 850kcal
특징: 대용량, 소고기, 베이컨, 치즈맛, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 99;

UPDATE products 
SET description = '몬스터 주니어버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 100;

UPDATE products 
SET description = '몬스터 주니어버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 101;

UPDATE products 
SET description = '바삭한 치킨패티 버거
재료: 바삭한 치킨 패티, 양상추, 마요네즈
칼로리: 580kcal
특징: 바삭함, 닭고기, 순한맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 102;

UPDATE products 
SET description = '치킨버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 103;

UPDATE products 
SET description = '치킨버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 104;

UPDATE products 
SET description = '치킨패티에 치즈와 마요가 들어간 버거' 
WHERE product_id = 105;

UPDATE products 
SET description = '치킨 치즈 마요 버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 106;

UPDATE products 
SET description = '치킨 치즈 마요 버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 107;

UPDATE products 
SET description = '킹 사이즈 치킨버거
재료: 킹 사이즈 치킨 패티, 양상추, 마요네즈
칼로리: 680kcal
특징: 대용량, 바삭함, 닭고기
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 108;

UPDATE products 
SET description = '치킨킹 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 109;

UPDATE products 
SET description = '치킨킹 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 110;

UPDATE products 
SET description = '치킨킹에 베이컨, 양상추, 토마토가 들어간 버거
재료: 킹 사이즈 치킨 패티, 베이컨, 양상추, 토마토, 마요네즈
칼로리: 780kcal
특징: 대용량, 바삭함, 닭고기, 베이컨
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 111;

UPDATE products 
SET description = '치킨킹BLT + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 112;

UPDATE products 
SET description = '치킨킹BLT + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 113;

UPDATE products 
SET description = '바삭한 새우패티 버거
재료: 바삭한 새우 패티, 양상추, 타르타르 소스
칼로리: 560kcal
특징: 바삭함, 새우, 해산물, 순한맛
알레르기: 갑각류, 밀, 계란, 대두' 
WHERE product_id = 114;

UPDATE products 
SET description = '슈림프버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 115;

UPDATE products 
SET description = '슈림프버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 116;

UPDATE products 
SET description = '통새우가 들어간 슈림프버거
재료: 바삭한 새우 패티, 통새우, 양상추, 타르타르 소스
칼로리: 620kcal
특징: 바삭함, 새우, 해산물, 통새우 식감
알레르기: 갑각류, 밀, 계란, 대두' 
WHERE product_id = 117;

UPDATE products 
SET description = '통새우슈림프버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 118;

UPDATE products 
SET description = '통새우슈림프버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 119;

UPDATE products 
SET description = '비프와 슈림프가 함께 들어간 버거' 
WHERE product_id = 120;

UPDATE products 
SET description = '비프&슈림프버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 121;

UPDATE products 
SET description = '비프&슈림프버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 122;

UPDATE products 
SET description = '바삭한 크리스퍼 클래식 버거
재료: 바삭한 치킨, 양상추, 마요네즈, 토마토
칼로리: 520kcal
특징: 매우 바삭함, 닭고기, 순한맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 123;

UPDATE products 
SET description = '크리스퍼 클래식 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 124;

UPDATE products 
SET description = '크리스퍼 클래식 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 125;

UPDATE products 
SET description = '크리스퍼 클래식에 베이컨, 양상추, 토마토가 들어간 버거
재료: 바삭한 치킨, 베이컨, 양상추, 토마토, 마요네즈
칼로리: 620kcal
특징: 매우 바삭함, 닭고기, 베이컨, 야채
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 126;

UPDATE products 
SET description = '크리스퍼 클래식 BLT + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 127;

UPDATE products 
SET description = '크리스퍼 클래식 BLT + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 128;

UPDATE products 
SET description = '매콤한 치폴레 소스의 크리스퍼 버거
재료: 바삭한 치킨, 치폴레 소스, 양상추, 토마토
칼로리: 580kcal
특징: 매우 바삭함, 닭고기, 매운맛, 치폴레향
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 129;

UPDATE products 
SET description = '크리스퍼 치폴레 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 130;

UPDATE products 
SET description = '크리스퍼 치폴레 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 131;

UPDATE products 
SET description = '마늘 소스가 들어간 크리스퍼 치킨버거
재료: 바삭한 치킨, 마늘 소스, 양상추
칼로리: 560kcal
특징: 매우 바삭함, 닭고기, 마늘향
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 132;

UPDATE products 
SET description = '크리스퍼 마늘 치킨 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 133;

UPDATE products 
SET description = '크리스퍼 마늘 치킨 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 134;

UPDATE products 
SET description = '크리스퍼 랩
재료: 바삭한 치킨, 양상추, 마요네즈, 토르티야
칼로리: 480kcal
특징: 매우 바삭함, 닭고기, 가볍게 먹기, 한 손으로 먹기 편함
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 135;

UPDATE products 
SET description = '치즈가 들어간 기본 버거
재료: 소고기 패티, 체다 치즈, 양상추, 토마토, 피클
칼로리: 400kcal
특징: 소고기, 치즈맛, 기본 버거
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 136;

UPDATE products 
SET description = '치즈버거 + 사이드 + 음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 137;

UPDATE products 
SET description = '치즈버거 + 라지사이드 + 라지음료 세트
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 138;

UPDATE products 
SET description = '더블 패티에 특제 소스가 들어간 프리미엄 버거
재료: 더블 소고기 패티, 특제 소스, 양상추, 토마토, 치즈
칼로리: 920kcal
특징: 프리미엄, 더블 패티, 특제 소스, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 139;

UPDATE products 
SET description = '더오치 맥시멈 원파운더 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 140;

UPDATE products 
SET description = '더오치 맥시멈 원파운더 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 141;

UPDATE products 
SET description = '더오치 맥시멈2 버거
재료: 더블 소고기 패티, 특제 소스, 양상추, 토마토, 치즈
칼로리: 920kcal
특징: 프리미엄, 더블 패티, 특제 소스, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 142;

UPDATE products 
SET description = '더오치 맥시멈2 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 143;

UPDATE products 
SET description = '더오치 맥시멈2 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 144;

UPDATE products 
SET description = '더오치 맥시멈3 버거
재료: 더블 소고기 패티, 특제 소스, 양상추, 토마토, 치즈
칼로리: 920kcal
특징: 프리미엄, 더블 패티, 특제 소스, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 145;

UPDATE products 
SET description = '더오치 맥시멈3 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 146;

UPDATE products 
SET description = '더오치 맥시멈3 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 147;

UPDATE products 
SET description = '트러플 소스와 머쉬룸이 들어간 더블 버거
재료: 더블 소고기 패티, 트러플 소스, 머쉬룸, 치즈
칼로리: 980kcal
특징: 고급 트러플향, 버섯, 더블 패티, 고칼로리
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 148;

UPDATE products 
SET description = '딥 트러플 머쉬룸 더블 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 149;

UPDATE products 
SET description = '딥 트러플 머쉬룸 더블 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 150;

UPDATE products 
SET description = '핫한 트러플 소스와 머쉬룸이 들어간 와퍼
재료: 불에 구운 소고기 패티, 트러플 소스, 머쉬룸, 치즈, 양상추
칼로리: 850kcal
특징: 불맛, 소고기, 고급 트러플향, 버섯, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 151;

UPDATE products 
SET description = '핫 트러플 머쉬룸 와퍼 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 152;

UPDATE products 
SET description = '핫 트러플 머쉬룸 와퍼 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 153;

UPDATE products 
SET description = '핫 트러플 머쉬룸 와퍼 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 154;

UPDATE products 
SET description = '트리플 머쉬룸이 들어간 와퍼
재료: 불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파, 케첩, 마요네즈
칼로리: 680kcal
특징: 불맛, 소고기, 신선한 야채
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 155;

UPDATE products 
SET description = '트리플 머쉬룸 와퍼 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 156;

UPDATE products 
SET description = '뉴욕 스테이크가 들어간 오리지널스 버거
재료: 뉴욕 스테이크, 양상추, 토마토, 특제 소스
칼로리: 820kcal
특징: 프리미엄, 스테이크, 고급 재료, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 157;

UPDATE products 
SET description = '오리지널스 뉴욕 스테이크 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 158;

UPDATE products 
SET description = '오리지널스 뉴욕 스테이크 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 159;

UPDATE products 
SET description = '메이플 갈릭 소스가 들어간 오리지널스 버거
재료: 소고기 패티, 메이플 갈릭 소스, 양상추, 베이컨
칼로리: 780kcal
특징: 프리미엄, 달콤함, 마늘향, 베이컨, 고칼로리
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 160;

UPDATE products 
SET description = '오리지널스 메이플 갈릭 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 161;

UPDATE products 
SET description = '오리지널스 메이플 갈릭 + 라지감자튀김 + 라지음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1300kcal (버거 포함)
특징: 세트 구성, 라지 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 162;

UPDATE products 
SET description = '오리지널스 메이플 갈릭 + 감자튀김 + 음료
구성: 버거 + 사이드 + 음료
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 163;

UPDATE products 
SET description = '트머와 팩 1번
구성: 트러플 머쉬룸 와퍼 패키지 메뉴
칼로리: 약 1200kcal
특징: 트러플향, 버섯, 패키지 구성
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 164;

UPDATE products 
SET description = '트머와 팩 2번
구성: 트러플 머쉬룸 와퍼 패키지 메뉴
칼로리: 약 1200kcal
특징: 트러플향, 버섯, 패키지 구성
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 165;

UPDATE products 
SET description = '트머와 팩 3번
구성: 트러플 머쉬룸 와퍼 패키지 메뉴
칼로리: 약 1200kcal
특징: 트러플향, 버섯, 패키지 구성
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 166;