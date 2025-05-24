import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://github.com/login"
driver.get(url)
time.sleep(2)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'login_field')
        self.password = (By.ID, 'password')
        self.login_button = (By.NAME, 'commit')

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(2)
        self.driver.find_element(*self.login_button).click()

login_page = LoginPage(driver)
login_page.login('rikesh', 'password')
time.sleep(2)

driver.quit()