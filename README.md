# 0. Getting Started (시작하기)
[참고 페이지] https://rahulshettyacademy.com/seleniumPractise/#/

<br/>
<br/>

# 1. Project Overview (프로젝트 개요)
- 프로젝트 이름: EndtoEnd Test 구현
- 프로젝트 설명: Pytest, Selenium을 활용한 e2e test 구현

<br/>
<br/>

# 2. Project Structure (프로젝트 구조)
```plaintext
project/
├── tests/
│   ├── conftest.py                    # 테스트 설정 파일
│   └── pastversion_of_endtoend.py     # 객체를 나누지 않은 Ver.
│   └── test_endtoend_class.py         # 객체를 나눈 최신 버전
├── utilities/  
│   ├── BaseClass.py                   # 최상단 클래스
├── Pages/          
│   ├── CheckOutPage.py                # 주문 확인 페이지 개체 모음
│   ├── CompletePage.py                # 마지막 페이지 개체 모음
│   ├── HomePage.py                    # 첫 페이지 개체 모음
│   ├── OrderPage.py                   # 주문 후 페이지 개체 모음
├── .gitignore                         # Git 무시 파일 목록
└── README.md                          # 프로젝트 개요 및 사용법
```

<br/>
<br/>

# 3. 테스트 시나리오
- 테스트는 간단한 시나리오만 작성하였습니다.
- 페이지에서 실제 이용자가 할 만한 시나리오를 예로 들었습니다.

1. 사이트 진입
2. 임의 야채 ADD TO CART
3. 사이트 스크롤 여러 번 진행
4. 검색 창에 “be” 검색
5. “Be”를 포함한 물품만 있는지 획인
6. 그 중 하나 제품 수량 2개 추가
7. 카트 클릭 후 제대로 담아졌는지 확인
8. PROCEED TO CHECKOUT
9. 담은 제품 들이 그대로 있는지 확인
10. Quantity, Price, Total 확인
11. Place Order
12. 모두 체크 후 Proceed
13. Thank You 확인
14. 끝.
