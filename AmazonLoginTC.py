from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# wait = WebDriverWait(driver,20)
driver.get("https://www.amazon.in/")
# driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='nav-link-accountList-nav-line-1']").click()

driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("7011996353")
driver.find_element(By.XPATH,"//input[@id='continue']").click()

driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("Rahul221@")

driver.find_element(By.XPATH,"//*[@id='signInSubmit']").click()
print("Login test case pass ")
driver.quit()