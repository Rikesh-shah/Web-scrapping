import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert"
driver.get(url)
time.sleep(2)

ifrane_element = driver.find_element(By.ID, 'iframeResult')
driver.switch_to.frame(ifrane_element)
time.sleep(2)

button = driver.find_element(By.XPATH, 'html/body/button')
button.click()
time.sleep(2)

print(f"Alert Text : ----------> {driver.switch_to.alert.text}")
alert = driver.switch_to.alert.accept()
time.sleep(2)

driver.switch_to.default_content()

driver.quit()