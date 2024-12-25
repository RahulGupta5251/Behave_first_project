from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,20)
act = ActionChains(driver)
try:
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    # Navigate to login page
    account_list = wait.until(EC.presence_of_element_located((By.ID,'nav-link-accountList-nav-line-1')))
    act.move_to_element(account_list).click().perform()
    # account_list.click()

    # ?Enter username and password 
    usernane = wait.until(EC.presence_of_element_located((By.ID,"ap_email")))
    usernane.clear()
    usernane.send_keys("7011996353")
    driver.find_element(By.ID,"continue").click()

    # Enter the password 
    password = wait.until(EC.visibility_of_element_located((By.ID,"ap_password")))
    password.clear()
    password.send_keys("Rahul221@",Keys.ENTER)

    print(driver.title)
    # pagetitle = wait.until(EC.title_contains("Online Shopping site in India"))
    assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" == driver.title

    # Navigate to specifiec section in the top navigation bar
    top_nav_bar = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id = 'nav-xshop']/a[5]")))
    act.move_to_element(top_nav_bar).click().perform()

    #scroll to the bottom of the page 
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    #Take a screenshot
    screenshotpath = "C:/Users/Rahul Gupta/BDDSeleniumframework/Screenshots/screenshot.png"
    driver.save_screenshot(screenshotpath)

except:
    print("Error observed , programm quit......")
finally:
    driver.quit()