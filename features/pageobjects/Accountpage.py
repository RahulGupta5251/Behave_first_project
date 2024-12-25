from selenium import webdriver
from selenium.webdriver.common.by import By

class Accountpage:

    def __init__(self,driver):
        self.driver = driver

    login_sucessfull_xpath = "//*[@id='content']/h2[1]"

    def loginsuccessverify(self):
        return self.driver.find_element(By.XPATH,self.login_sucessfull_xpath).is_displayed()