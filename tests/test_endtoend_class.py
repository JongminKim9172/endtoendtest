import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from Pages.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestEndToEnd(BaseClass):

    @pytest.fixture(params=[("Brocolli - 1 Kg", "Cucumber - 1 Kg", "Beetroot - 1 Kg")])
    def getData(self, request):
        # request.param은 현재 grouped_data에서 전달된 하나의 튜플 값
        return request.param

    def test_endtoend(self, getData):
        # 시작 전 로그 받는 작업
        log = self.get_logger()

        # 1. 사이트 진입
        homepage = HomePage(self.driver)

        # 2. 임의 야채 ADD TO CART
        vegetables = homepage.cart()
        log.info("Vegetables 중 2가지를 Add To Cart")
        log.info(getData)

        for vegetable in vegetables:  # vegetables 리스트를 순회한다고 가정
            vegetable_name = vegetable.find_element(By.XPATH, "h4").text

            # 필요한 작업을 하나의 조건문으로 처리
            if getData[0] in vegetable_name:
                vegetable.find_element(By.XPATH, "div/button").click()
            elif getData[1] in vegetable_name:
                vegetable.find_element(By.XPATH, "div/a[@class='increment']").click()
                vegetable.find_element(By.XPATH, "div/button").click()

        # 3. 사이트 스크롤 여러 번 진행
        for scroll in BaseClass.scroll:
            self.driver.execute_script(scroll)
            time.sleep(1)

        # 4. 검색 창에 “be” 검색
        homepage.search().send_keys(getData[2][:2].lower())

        # 5. “Be”를 포함한 물품만 있는지 획인
        # 6. 그 중 하나 제품 수량 2개 추가
        vegetables = homepage.cart()

        for vegetable in vegetables:
            assert getData[2][:2].lower() in vegetable.find_element(By.XPATH, "h4").text.lower(), f"'{vegetable.find_element(By.XPATH, "h4").text}' 'be'를 포함하지 않음."

            if getData[2] in vegetable.find_element(By.XPATH, "h4").text:
                for i in range(2):
                    vegetable.find_element(By.XPATH, "div/a[@class='increment']").click()
                vegetable.find_element(By.XPATH, "div/button").click()

        # 7. 카트 클릭 후 제대로 담아졌는지 확인
        homepage.cart_click().click()

        # 8. 담은 제품 들이 그대로 있는지 확인
        checkout_products = homepage.checkout_popup()

        for checkout_product in checkout_products:
            assert checkout_product.text in getData

        # 9. PROCEED TO CHECKOUT
        log.info("PROCEED TO CHECKOUT")
        checkoutpage = homepage.proceed_to_checkout()

        # 10. Quantity, Price, Total 확인
        tables_td = checkoutpage.tables()
        total_price = 0

        for i in range(1, len(tables_td), 4):
            quantity = int(tables_td[i].text)
            price = float(tables_td[i + 1].text)
            total = float(tables_td[i + 2].text)
            total_price += total

        assert abs(quantity * price - total) < 1, f"숫자가 맞지 않음. {i}: {quantity} * {price} != {total}"

        # 표에 있는 금액과 하단 Total Amount와 금액이 같은지 확인
        assert abs(total_price - int(checkoutpage.totalAmount())) < 1, "상단 금액과 하단 금액이 맞지 않음"

        # 11. Place Order
        log.info("Place Order")
        orderpage = checkoutpage.placeOrder()

        # 12. 모두 체크 후 Proceed
        countries = orderpage.select_countries()

        for country in countries:
            if country.text == "South Korea":
                country.click()

        orderpage.agree().click()
        completepage = orderpage.proceed()
        log.info("Complete Page")

        # 13. Thank You 확인
        thank_you_element = completepage.complete()
        assert "Thank you" in thank_you_element.text