from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains


class seleniumhelper:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,page_url):
        self.driver.get(page_url)

    def orange_url(self,orange_url):
        self.driver.get(orange_url)