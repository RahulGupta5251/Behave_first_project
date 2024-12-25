from behave import *
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from Helper.seleniumhelper import seleniumhelper

@given("chrome driver launch")
def given_imp(context):
    print("this is when method ")
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
@when("Enter valid credential '{username}' and '{password}' valuesss")
def when_imple(context,username,password):
    context.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)
@then("Varify logo")
def then_imple(context):
    time.sleep(3)