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

"""
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
"""
class TestEndToEnd(BaseClass):
    def test_endtoend(self):
        customer_want = ["Brocolli - 1 Kg", "Cucumber - 1 Kg", "Beetroot - 1 Kg"]

        # 1. 사이트 진입
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)

        # 2. 임의 야채 ADD TO CART
        vegetables = driver.find_elements(By.XPATH, "//div[@class='product']")

        for vegetable in vegetables:
            if "Brocolli" in vegetable.find_element(By.XPATH, "h4").text:
                customer_want.append(vegetable.find_element(By.XPATH, "h4").text)
                vegetable.find_element(By.XPATH, "div/button").click()

            if "Cucumber" in vegetable.find_element(By.XPATH, "h4").text:
                customer_want.append(vegetable.find_element(By.XPATH, "h4").text)
                vegetable.find_element(By.XPATH, "div/a[@class='increment']").click()
                vegetable.find_element(By.XPATH, "div/button").click()

        # 3. 사이트 스크롤 여러 번 진행
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # 4. 검색 창에 “be” 검색
        driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("be")

        vegetables = driver.find_elements(By.XPATH, "//div[@class='product']")

        # 5. “Be”를 포함한 물품만 있는지 획인
        for vegetable in vegetables:
            # h4_vegetables = vegetable.find_element(By.XPATH, "h4")
            # for h4_vegetable in h4_vegetables:
            assert "be" in vegetable.find_element(By.XPATH,"h4").text.lower(), f"'{vegetable.find_element(By.XPATH, "h4").text}' does not contain 'be'"

            if "Beetroot" in vegetable.find_element(By.XPATH, "h4").text:
                for i in range(2):
                    vegetable.find_element(By.XPATH, "div/a[@class='increment']").click()
                vegetable.find_element(By.XPATH, "div/button").click()

        # 6. 그 중 하나 제품 수량 2개 추가



        # 7. 카트 클릭 후 제대로 담아졌는지 확인
        driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()

        # 8. 담은 제품 들이 그대로 있는지 확인
        checkout_products = driver.find_elements(By.XPATH, "(//ul)[1]/li/div/p[@class='product-name']")

        for checkout_product in checkout_products:
            assert checkout_product.text in customer_want

        # 9. PROCEED TO CHECKOUT
        place_order_button = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
        assert place_order_button.is_enabled(), "Proceed to checkout 버튼이 활성화 안 됨."
        place_order_button.click()

        # 10. Quantity, Price, Total 확인
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다림
        calculator = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td/p")))

        num_calculator_elements = len(calculator)
        total_price = 0

        for i in range(1, num_calculator_elements, 4):
            quantity = int(calculator[i].text)
            price = float(calculator[i + 1].text)
            total = float(calculator[i + 2].text)
            total_price += total

        assert abs(quantity * price - total) < 1, f"Mismatch at index {i}: {quantity} * {price} != {total}"

        # 표에 있는 금액과 하단 Total Amount와 금액이 같은지 확인
        assert abs(total_price - int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)) < 1, "상단 금액과 하단 금액이 맞지 않음"

        # 11. Place Order
        driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

        # 12. 모두 체크 후 Proceed
        driver.find_element(By.XPATH, "//select").click()
        countries = driver.find_elements(By.XPATH, "//select/option")

        for country in countries:
            if country.text == "South Korea":
                country.click()

        driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
        driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

        # 13. Thank You 확인
        thank_you_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you')]"))
        )

        assert "Thank you" in thank_you_element.text

        # 14. 끝.
        driver.quit()