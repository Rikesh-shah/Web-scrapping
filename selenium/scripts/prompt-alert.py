import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt"
driver.get(url)
time.sleep(2)

iframe_element = driver.find_element(By.ID, 'iframeResult')
driver.switch_to.frame(iframe_element)

button = driver.find_element(By.XPATH, '/html/body/button')
button.click()

print(f"Prompt alert text ------------> {driver.switch_to.alert.text}")

driver.switch_to.alert.send_keys("Rikesh")
time.sleep(2)
# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.switch_to.default_content()

driver.quit()