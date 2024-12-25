from selenium import webdriver
from behave import *
from pageobjects.MMThomepage import MMTHomepage
import time 
@given("I naviagted to MMT Home  page")
def step_impl(context):
    
    mhp = MMTHomepage(context.driver)
    mhp.close_popup()
    time.sleep(5)
    

@when("Select FROM option")
def step_impl(context):
    mhp = MMTHomepage(context.driver)
    mhp.From_click()
    time.sleep(3)
    mhp.select_from_option()
    time.sleep(8)

@step("Select To option")
def step_impl(context):
    mhp = MMTHomepage(context.driver)
    mhp.To_click()
    mhp.select_To_option()
    time.sleep(2)

@step("Select Departure")
def step_impl(context):
    mhp = MMTHomepage(context.driver)
    mhp.date_select_method()
    time.sleep(2)
    


@step("click Search  button")
def step_impl(context):
    mhp = MMTHomepage(context.driver)
    mhp.searchbutton_method()
    time.sleep(2)
    

@then("Click on View Prices")
def step_imple(context):
    print("Then method implementation")
