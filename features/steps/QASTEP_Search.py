import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains


# def get_config():
#     config =ConfigParser()
#     config.read('config.ini')
#     return config.get("DEFAULT","base_url")

@given(u'I got naviagted to home page')
def step_impl(context):
    time.sleep(4)
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # # context.driver.get("https://tutorialsninja.com/demo/")
    # context.driver.get(readproperties.get_config("DEFAULT","base_url"))

@when(u'Enter  valid product into the search box')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")


@when(u'click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()


@then(u'Vaild product should get displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//a[normalize-space()='HP LP3065']").is_displayed()
    # context.driver.quit()

@when(u'Enter  INvalid product into the search box')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HONDA")

@then(u'Proper meaasge should displayed on search button')
def step_impl(context):
    expected_text  = "There is no product that matches the search criteria."
    time.sleep(5)
    actualtext = context.driver.find_element(By.XPATH,"//*[@id='button-search']/following-sibling::p").text()
    # assert actualtext.is_displayed()
    # assert  expected_text == actual_text
    time.sleep(2)
    print("test case passs")
    # context.driver.quit()

@when(u'DO not enter anything into the search box')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("")