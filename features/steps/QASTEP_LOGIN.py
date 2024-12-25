import time
from datetime import datetime
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from pageobjects.Homepage import Homepage
from pageobjects.Loginpage import Loginpage
from pageobjects.Accountpage import Accountpage
# from utilities import xyz
@given(u'I naviagted to Login page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")
    # context.driver.get(xyz.get_config("DEFAULT","url"))
    # context.driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
    

    hp = Homepage(context.driver)
    hp.click_on_my_account()
    hp.select_login_option()
    # context.driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()

@when(u'Enter  valid Email And Vaild Password')
def step_impl(context):
    lp = Loginpage(context.driver)
    lp.enter_email_address("qwerty987654321@gmail.com")
    lp.enter_password_address("qwe@123")
    # context.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("qwerty987654321@gmail.com")
    time.sleep(1)
    # context.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("qwe@123")


@when(u'click Login button')
def step_impl(context):
    lp = Loginpage(context.driver)
    lp.enter_login_button()
    # context.driver.find_element(By.XPATH,"//input[@value='Login']").click()


@then(u'Login successfull')
def step_impl(context):
    ap = Accountpage(context.driver)
    # assert context.driver.find_element(By.XPATH,"//*[@id='content']/h2[1]").is_displayed()
    assert ap.loginsuccessverify()
    time.sleep(2)
    # context.driver.quit()


@when(u'Enter Invalid Email and vaild password')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sachin"+time_stamp+"@gmail.com"
    lp = Loginpage(context.driver)
    lp.enter_email_address(invalid_email)
    time.sleep(2)
    lp.enter_password_address("qwe@123")

    # context.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("qwerty987654321@gml.com")
    # time.sleep(1)
    # context.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("qwe@123")


@then(u'Proper Warning message displayed')
def step_impl(context):
    lp = Loginpage(context.driver)
    time.sleep(2)
    assert lp.warningmessageverify()

    # assert context.driver.find_element(By.XPATH,"//*[@id='account-login']/div[1]").is_displayed()
    # time.sleep(2)
    # context.driver.quit()


@when(u'Enter valid Email and INvaild password')
def step_impl(context):

    lp = Loginpage(context.driver)
    lp.enter_email_address("qwerty987654321@gmail.com")
    time.sleep(2)
    lp.enter_password_address("qwe@1")


    # context.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("qwerty987654321@gmail.com")
    # time.sleep(2)
    # context.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("qwe@12")


@when(u'Enter INvalid Email and INvaild password')
def step_impl(context):

    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sachin"+time_stamp+"@gmail.com"
    lp = Loginpage(context.driver)
    lp.enter_email_address(invalid_email)
    time.sleep(2)
    lp.enter_password_address("q")

    # context.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("qwerty987654321@gm.com")
    # time.sleep(2)
    # context.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("qwe")