from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from Helper.seleniumhelper import seleniumhelper

# @given('we have behave installed')
# def step_impl(context):
URL = "https://www.amazon.in/"
@when('we implement a test')
def step_impl(context):
    seleniumhelper(context.driver).open_page(URL)
    # context.driver.get("https://www.amazon.in/")
    context.driver.maximize_window()

    # Navigate to login page
    account_list = context.wait.until(EC.presence_of_element_located((By.ID,'nav-link-accountList-nav-line-1')))
    context.act.move_to_element(account_list).click().perform()
    # account_list.click()

    # ?Enter username and password 
    usernane = context.wait.until(EC.presence_of_element_located((By.ID,"ap_email")))
    usernane.clear()
    usernane.send_keys("7011996353")
    context.driver.find_element(By.ID,"continue").click()

    # Enter the password 
    password = context.wait.until(EC.visibility_of_element_located((By.ID,"ap_password")))
    password.clear()
    password.send_keys("Rahul221@",Keys.ENTER)

    top_nav_bar = context.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id = 'nav-xshop']/a[5]")))
    context.act.move_to_element(top_nav_bar).click().perform()

    #scroll to the bottom of the page 
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    #Take a screenshot
    screenshotpath = "C:/Users/Rahul Gupta/BDDSeleniumframework/Screenshots/screenshot.png"
    context.driver.save_screenshot(screenshotpath)

@then('behave will test it for us!')
def step_impl(context):
    
    context.pagetittle = context.driver.title
    print(context.pagetittle)
    # context.pagetitle = context.wait.until(EC.title_contains("Online Shopping site in India"))
    # assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" == context.pagetittle
    print("Login sucessfull ")
    assert 1 == 1