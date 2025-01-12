import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.OrderPage import OrderPage


class CheckOutPage():

    tables_td = (By.XPATH, "//td/p")
    total_amount = (By.CSS_SELECTOR, ".totAmt")
    place_order_button = (By.XPATH, "//button[text()='Place Order']")


    def __init__(self, driver):
        self.driver = driver

    def tables(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(CheckOutPage.tables_td))

    def totalAmount(self):
        return self.driver.find_element(*CheckOutPage.total_amount).text

    def placeOrder(self):
        self.driver.find_element(*CheckOutPage.place_order_button).click()
        orderpage = OrderPage(self.driver)
        return orderpage
