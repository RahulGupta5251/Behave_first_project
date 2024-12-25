from selenium import webdriver
from selenium.webdriver.common.by import By
class Homepage:

    def __init__(self,driver):
        self.driver = driver

    myaccount_xpath = "//span[normalize-space()='My Account']"
    Login_xpath = "//a[normalize-space()='Login']"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH,self.myaccount_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.XPATH,self.Login_xpath).click()