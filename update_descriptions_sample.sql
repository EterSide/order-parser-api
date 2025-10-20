-- 제품 Description 업데이트 SQL (샘플)
-- 재료, 칼로리, 특징, 알레르기 정보 추가
-- 실제 사용 시 전체 제품에 대해 적용 필요

-- =================================
-- 1. 음료 (저칼로리 / 제로칼로리)
-- =================================

-- 미네랄워터
UPDATE products 
SET description = '깨끗한 미네랄워터
재료: 천연 미네랄워터
칼로리: 0kcal
특징: 무칼로리, 수분보충, 다이어트
알레르기: 없음' 
WHERE product_id = 1;

-- 코카콜라 제로 (R)
UPDATE products 
SET description = '칼로리 제로 코카콜라 (R)
재료: 탄산수, 콜라향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 클래식 콜라맛, 다이어트
알레르기: 없음' 
WHERE product_id = 19;

-- 스프라이트 제로 (R)
UPDATE products 
SET description = '칼로리 제로 라임맛 탄산음료 (R)
재료: 탄산수, 라임향, 인공감미료
칼로리: 0kcal
특징: 제로칼로리, 라임향, 청량감, 다이어트
알레르기: 없음' 
WHERE product_id = 4;

-- 코카콜라 (R)
UPDATE products 
SET description = '시원한 코카콜라 (R)
재료: 탄산수, 설탕, 콜라향
칼로리: 200kcal
특징: 클래식 콜라맛, 청량감
알레르기: 없음' 
WHERE product_id = 17;

-- 아이스아메리카노
UPDATE products 
SET description = '시원한 아메리카노
재료: 에스프레소, 물, 얼음
칼로리: 5kcal
특징: 저칼로리, 커피향, 카페인, 시원함, 다이어트
알레르기: 없음' 
WHERE product_id = 9;

-- 미닛메이드 오렌지
UPDATE products 
SET description = '상큼한 오렌지 주스
재료: 오렌지 농축액, 비타민C
칼로리: 180kcal
특징: 비타민C 풍부, 상큼한 맛, 과일
알레르기: 없음' 
WHERE product_id = 2;

-- =================================
-- 2. 디저트 (고칼로리)
-- =================================

-- 초코 선데
UPDATE products 
SET description = '초콜릿 선데이
재료: 아이스크림, 초콜릿 시럽
칼로리: 380kcal
특징: 달콤함, 초콜릿맛, 디저트
알레르기: 우유, 대두' 
WHERE product_id = 13;

-- 초코 브라우니 킹퓨전
UPDATE products 
SET description = '초콜릿 브라우니 킹퓨전
재료: 아이스크림, 초콜릿 브라우니, 초콜릿 시럽
칼로리: 520kcal
특징: 고칼로리, 달콤함, 초콜릿, 브라우니 식감, 디저트
알레르기: 우유, 밀, 계란, 대두' 
WHERE product_id = 14;

-- =================================
-- 3. 소스 및 시즈닝
-- =================================

-- 디아블로소스 (매운맛)
UPDATE products 
SET description = '매운 디아블로 소스
재료: 칠리, 핫소스, 향신료
칼로리: 25kcal
특징: 매운맛, 불맛, 저칼로리
알레르기: 없음' 
WHERE product_id = 26;

-- 허니머스타드소스
UPDATE products 
SET description = '달콤한 허니머스타드 소스
재료: 꿀, 머스타드, 마요네즈
칼로리: 80kcal
특징: 달콤함, 새콤함, 디핑소스
알레르기: 계란, 대두' 
WHERE product_id = 25;

-- =================================
-- 4. 사이드 (저칼로리 vs 고칼로리)
-- =================================

-- 코울슬로 (저칼로리, 채소)
UPDATE products 
SET description = '신선한 코울슬로 샐러드
재료: 양배추, 당근, 마요네즈, 식초
칼로리: 150kcal
특징: 저칼로리, 신선함, 채소, 새콤달콤, 다이어트
알레르기: 계란, 대두' 
WHERE product_id = 28;

-- 콘샐러드 (저칼로리, 채소)
UPDATE products 
SET description = '달콤한 콘샐러드
재료: 옥수수, 마요네즈, 설탕
칼로리: 180kcal
특징: 저칼로리, 달콤함, 채소, 다이어트
알레르기: 계란, 대두' 
WHERE product_id = 29;

-- 프렌치프라이 (R)
UPDATE products 
SET description = '바삭한 프렌치프라이 (R)
재료: 감자, 식물성 기름, 소금
칼로리: 340kcal
특징: 바삭함, 짭짤함, 감자맛
알레르기: 없음' 
WHERE product_id = 31;

-- 프렌치프라이 (L)
UPDATE products 
SET description = '바삭한 프렌치프라이 (L)
재료: 감자, 식물성 기름, 소금
칼로리: 480kcal
특징: 바삭함, 짭짤함, 감자맛, 대용량
알레르기: 없음' 
WHERE product_id = 30;

-- 21치즈스틱 (고단백, 치즈)
UPDATE products 
SET description = '21가지 치즈가 들어간 치즈스틱
재료: 21가지 치즈 블렌드, 빵가루
칼로리: 420kcal
특징: 쫄깃함, 진한 치즈맛, 고단백
알레르기: 우유, 밀, 대두' 
WHERE product_id = 36;

-- 크리미모짜볼 (5조각)
UPDATE products 
SET description = '크리미한 모짜렐라 치즈볼 5조각
재료: 모짜렐라 치즈, 빵가루
칼로리: 290kcal
특징: 쫄깃함, 크리미함, 치즈맛, 고단백
알레르기: 우유, 밀, 대두' 
WHERE product_id = 38;

-- 코코넛슈림프 (6조각)
UPDATE products 
SET description = '코코넛 튀김 새우 6조각 + 스위트칠리소스
재료: 새우, 코코넛 빵가루, 스위트칠리소스
칼로리: 430kcal
특징: 바삭함, 코코넛향, 새우맛, 달콤한 소스, 해산물
알레르기: 갑각류, 밀, 대두' 
WHERE product_id = 39;

-- 바삭킹 8조각 + 디아블로소스 (매운맛)
UPDATE products 
SET description = '바삭한 치킨 8조각 + 디아블로소스
재료: 치킨, 디아블로소스 (매운맛)
칼로리: 620kcal
특징: 바삭함, 닭고기, 고단백, 매운맛, 불맛
알레르기: 밀, 대두, 계란' 
WHERE product_id = 43;

-- 너겟킹 4조각 (순한맛)
UPDATE products 
SET description = '바삭한 치킨너겟 4조각
재료: 닭가슴살, 빵가루
칼로리: 190kcal
특징: 바삭함, 닭고기, 고단백, 순한맛, 어린이
알레르기: 밀, 대두, 계란' 
WHERE product_id = 48;

-- 리얼어니언링 (R)
UPDATE products 
SET description = '진짜 양파로 만든 어니언링 (R)
재료: 진짜 양파, 빵가루
칼로리: 280kcal
특징: 바삭함, 양파맛, 고소함
알레르기: 밀, 대두' 
WHERE product_id = 49;

-- =================================
-- 5. 버거 - 와퍼 시리즈
-- =================================

-- 와퍼 (클래식, 불맛)
UPDATE products 
SET description = '클래식 와퍼
재료: 불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파, 케첩, 마요네즈
칼로리: 680kcal
특징: 불맛, 소고기, 신선한 야채
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 52;

-- 와퍼 세트
UPDATE products 
SET description = '와퍼 + 사이드 + 음료 세트
구성: 와퍼 버거 + 프렌치프라이(R) + 코카콜라(R)
칼로리: 약 1100kcal (버거 포함)
특징: 세트 구성, 레귤러 사이즈, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 53;

-- 불고기와퍼 (달콤한 맛)
UPDATE products 
SET description = '달콤한 불고기 소스의 와퍼
재료: 불에 구운 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 720kcal
특징: 불맛, 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 55;

-- 치즈와퍼 (치즈 듬뿍)
UPDATE products 
SET description = '치즈가 들어간 와퍼
재료: 불에 구운 소고기 패티, 체다 치즈, 양상추, 토마토, 피클, 양파
칼로리: 730kcal
특징: 불맛, 소고기, 진한 치즈맛
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 61;

-- 콰트로치즈와퍼 (치즈 4가지)
UPDATE products 
SET description = '4가지 치즈가 들어간 와퍼
재료: 불에 구운 소고기 패티, 4가지 치즈 (체다, 모짜렐라, 에멘탈, 파마산), 양상추
칼로리: 880kcal
특징: 불맛, 소고기, 진한 치즈맛, 고칼로리, 치즈 듬뿍
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 67;

-- 통새우와퍼 (해산물)
UPDATE products 
SET description = '통새우가 들어간 와퍼
재료: 불에 구운 소고기 패티, 통새우, 양상추, 타르타르 소스
칼로리: 760kcal
특징: 불맛, 소고기, 새우, 해산물
알레르기: 갑각류, 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 70;

-- 트러플 머쉬룸 와퍼 (프리미엄, 고급)
UPDATE products 
SET description = '트러플 소스와 머쉬룸이 들어간 와퍼
재료: 불에 구운 소고기 패티, 트러플 소스, 머쉬룸, 치즈, 양상추
칼로리: 850kcal
특징: 불맛, 소고기, 고급 트러플향, 버섯, 고칼로리, 프리미엄
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 73;

-- 몬스터와퍼 (대용량, 고칼로리)
UPDATE products 
SET description = '대용량 몬스터와퍼
재료: 불에 구운 대용량 소고기 패티, 베이컨, 치즈, 양상추, 토마토
칼로리: 1200kcal
특징: 불맛, 소고기, 대용량, 고칼로리, 배불리 먹기
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 76;

-- 와퍼주니어 (소형, 어린이)
UPDATE products 
SET description = '기본 와퍼 주니어
재료: 불에 구운 소고기 패티, 양상추, 토마토, 피클, 양파
칼로리: 410kcal
특징: 불맛, 소고기, 작은 사이즈, 가볍게 먹기, 어린이
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 79;

-- =================================
-- 6. 버거 - 치킨 시리즈
-- =================================

-- 치킨버거 (순한맛)
UPDATE products 
SET description = '바삭한 치킨패티 버거
재료: 바삭한 치킨 패티, 양상추, 마요네즈
칼로리: 580kcal
특징: 바삭함, 닭고기, 순한맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 102;

-- 치킨킹 (대용량 치킨)
UPDATE products 
SET description = '킹 사이즈 치킨버거
재료: 킹 사이즈 치킨 패티, 양상추, 마요네즈
칼로리: 680kcal
특징: 대용량, 바삭함, 닭고기
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 108;

-- 치킨킹BLT (베이컨, 야채)
UPDATE products 
SET description = '치킨킹에 베이컨, 양상추, 토마토가 들어간 버거
재료: 킹 사이즈 치킨 패티, 베이컨, 양상추, 토마토, 마요네즈
칼로리: 780kcal
특징: 대용량, 바삭함, 닭고기, 베이컨, 야채
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 111;

-- 크리스퍼 클래식 (매우 바삭)
UPDATE products 
SET description = '바삭한 크리스퍼 클래식 버거
재료: 바삭한 치킨, 양상추, 마요네즈, 토마토
칼로리: 520kcal
특징: 매우 바삭함, 닭고기, 순한맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 123;

-- 크리스퍼 치폴레 (매운맛)
UPDATE products 
SET description = '매콤한 치폴레 소스의 크리스퍼 버거
재료: 바삭한 치킨, 치폴레 소스, 양상추, 토마토
칼로리: 580kcal
특징: 매우 바삭함, 닭고기, 매운맛, 치폴레향
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 129;

-- 크리스퍼 랩 (가볍게, 한손)
UPDATE products 
SET description = '크리스퍼 랩
재료: 바삭한 치킨, 양상추, 마요네즈, 토르티야
칼로리: 480kcal
특징: 매우 바삭함, 닭고기, 가볍게 먹기, 한 손으로 먹기 편함
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 135;

-- =================================
-- 7. 버거 - 슈림프/비프 시리즈
-- =================================

-- 슈림프버거 (해산물)
UPDATE products 
SET description = '바삭한 새우패티 버거
재료: 바삭한 새우 패티, 양상추, 타르타르 소스
칼로리: 560kcal
특징: 바삭함, 새우, 해산물, 순한맛
알레르기: 갑각류, 밀, 계란, 대두' 
WHERE product_id = 114;

-- 통새우슈림프버거 (통새우)
UPDATE products 
SET description = '통새우가 들어간 슈림프버거
재료: 바삭한 새우 패티, 통새우, 양상추, 타르타르 소스
칼로리: 620kcal
특징: 바삭함, 새우, 해산물, 통새우 식감
알레르기: 갑각류, 밀, 계란, 대두' 
WHERE product_id = 117;

-- 비프불고기버거 (달콤)
UPDATE products 
SET description = '달콤한 불고기 소스의 비프버거
재료: 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 620kcal
특징: 소고기, 달콤한 불고기맛
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 93;

-- 더블비프불고기버거 (더블 패티)
UPDATE products 
SET description = '더블 패티 비프불고기버거
재료: 더블 소고기 패티, 불고기 소스, 양상추, 양파
칼로리: 920kcal
특징: 소고기, 달콤한 불고기맛, 더블 패티, 고칼로리
알레르기: 밀, 계란, 우유, 대두' 
WHERE product_id = 96;

-- =================================
-- 8. 프리미엄 버거
-- =================================

-- 오리지널스 뉴욕 스테이크 (프리미엄)
UPDATE products 
SET description = '뉴욕 스테이크가 들어간 오리지널스 버거
재료: 뉴욕 스테이크, 양상추, 토마토, 특제 소스
칼로리: 820kcal
특징: 프리미엄, 스테이크, 고급 재료, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 157;

-- 더오치 맥시멈 원파운더 (프리미엄, 대용량)
UPDATE products 
SET description = '더블 패티에 특제 소스가 들어간 프리미엄 버거
재료: 더블 소고기 패티, 특제 소스, 양상추, 토마토, 치즈
칼로리: 920kcal
특징: 프리미엄, 더블 패티, 특제 소스, 고칼로리
알레르기: 밀, 계란, 우유, 대두, 토마토' 
WHERE product_id = 139;

-- =================================
-- 적용 방법
-- =================================

-- 1. MySQL/MariaDB:
--    mysql -u username -p database_name < update_descriptions_sample.sql

-- 2. PostgreSQL:
--    psql -U username -d database_name -f update_descriptions_sample.sql

-- 3. SQLite:
--    sqlite3 database.db < update_descriptions_sample.sql

-- 4. 또는 DB 클라이언트에서 직접 복사하여 실행

-- =================================
-- 참고사항
-- =================================

-- 이것은 샘플입니다. 전체 166개 제품에 대해 동일한 방식으로 적용하세요.
-- update_descriptions.py 스크립트를 실행하면 전체 제품에 대한 SQL이 생성됩니다.

