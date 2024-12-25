from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.support.ui import WebDriverWait

from utilities import xyz   ## use this 
### config parser function is in XYZ.py file , pleasecheck it first 
def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    # context.driver.get("https://tutorialsninja.com/demo/")
    # context.driver.get(xyz.get_config("DEFAULT","url"))     ## use this  for QA fox
    context.driver.get(xyz.get_config("Makemytrip","mmt_url"))

def after_scenario(context,scenario):
    time.sleep(4)
    context.driver.quit()








# def before_freature(context,feature):
#     print("this is before feature method") 

# def before_scenario(context,scenario):
#     print("This is before scenario method")
#     context.driver = webdriver.Chrome()
#     context.driver.implicitly_wait(10)
#     context.driver.maximize_window()

# def after_scenario(context,scenario):
#     print("Chrome driverclosed.......")
#     context.driver.quit()
