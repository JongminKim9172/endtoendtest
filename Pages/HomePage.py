import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from Pages.CheckOutPage import CheckOutPage


class HomePage:
    add_to_cart = (By.XPATH, "//div[@class='product']")
    search_keyword = (By.CSS_SELECTOR, ".search-keyword")
    cart_icon = (By.CSS_SELECTOR, ".cart-icon")
    checkout = (By.XPATH, "(//ul)[1]/li/div/p[@class='product-name']")
    proceed_to_checkout_button = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def cart(self):
        return self.driver.find_elements(*HomePage.add_to_cart)

    def search(self):
        return self.driver.find_element(*HomePage.search_keyword)

    def cart_click(self):
        return self.driver.find_element(*HomePage.cart_icon)

    def checkout_popup(self):
        return self.driver.find_elements(*HomePage.checkout)

    def proceed_to_checkout(self):
        self.driver.find_element(*HomePage.proceed_to_checkout_button).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage