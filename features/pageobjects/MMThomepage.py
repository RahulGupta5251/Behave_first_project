from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from Helper.seleniumhelper import seleniumhelper

class MMTHomepage:

    def __init__(self,driver):
        self.driver = driver
    
    cross_button_xpath = "//span[@class='commonModal__close']"
    From_click_xpath = "//*[@id='top-banner']/div[2]/div/div/div/div/div[2]/div[1]/div[1]/label"
    bangkok_from_xpath = "//li[@id='react-autowhatever-1-section-0-item-2']//div[@class='makeFlex column flexOne appendRight10']"
    To_click_xpath = "//span[normalize-space()='To']"
    mumbai_to_xpath =   "(//p[text() = 'Mumbai, India'])[1]"
    empty_click_xpath = "//*[@id='top-banner']/div[2]/div/div/div/div"
    Departure_click_xpath = "//span[text() = 'Departure']"
    dateselect_xpath   = "//*[@id='top-banner']/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div/p[1]"
    forward_click_xpath = "//span[@aria-label='Next Month']"
    january_8_xpath = "(//p[text() = '8'])[1]"
    search_button_xpath = "//a[text() ='Search']"
    view_price_xpath = "//*[@id='bookbutton-RKEY:1f7e03a0-474c-4d1b-a5cb-3994896f5efb:256_0']"

    def close_popup(self):
        self.driver.find_element(By.XPATH,self.cross_button_xpath).click()

    def From_click(self):
        self.driver.find_element(By.XPATH,self.From_click_xpath).click()

    def select_from_option(self):
        self.driver.find_element(By.XPATH,self.bangkok_from_xpath).click()

    def To_click(self):
        self.driver.find_element(By.XPATH,self.To_click_xpath).click()
    
    def select_To_option(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.mumbai_to_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.empty_click_xpath).click()
    def departure_click(self):
        self.driver.find_element(By.XPATH,self.Departure_click_xpath).click()
        time.sleep(2)
    def date_select_method(self):
        self.driver.find_element(By.XPATH ,self.forward_click_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.january_8_xpath).click()
        time.sleep(2)

    def searchbutton_method(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
        time.sleep(3)
    def view_price_method(self):
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.presence_of_all_elements_located((By.XPATH,self.view_price_xpath))).click()
        # self.driver.find_element().click()
        time.sleep(10)
