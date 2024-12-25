from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Loginpage:
    
    def __init__(self,driver):
        self.driver = driver

    email_address_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    warningmessage_xpath = "//*[@id='account-login']/div[1]"

    def enter_email_address(self,email):
        self.driver.find_element(By.XPATH,self.email_address_field_xpath).send_keys(email)

    def enter_password_address(self,password):
        self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(password)

    def enter_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        time.sleep(2)

    def warningmessageverify(self):
        return self.driver.find_element(By.XPATH,self.warningmessage_xpath).is_displayed()