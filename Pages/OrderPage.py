import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.CompletePage import CompletePage


class OrderPage:

    select = (By.XPATH, "//select")
    countries = (By.XPATH, "//select/option")
    agree_button = (By.CSS_SELECTOR, ".chkAgree")
    proceed_button = (By.XPATH, "//button[text()='Proceed']")

    def __init__(self, driver):
        self.driver = driver

    def select_countries(self):
        self.driver.find_element(*OrderPage.select).click()
        return self.driver.find_elements(*OrderPage.countries)

    def agree(self):
        return self.driver.find_element(*OrderPage.agree_button)

    def proceed(self):
        self.driver.find_element(*OrderPage.proceed_button).click()
        completepage = CompletePage(self.driver)
        return completepage
