import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompletePage():

    complete_word = (By.XPATH, "//*[contains(text(), 'Thank you')]")

    def __init__(self, driver):
        self.driver = driver

    def complete(self):
        return WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located(CompletePage.complete_word))