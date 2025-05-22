import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm"
driver.get(url)
time.sleep(2)

iframe_element = driver.find_element(By.ID, 'iframeResult')
driver.switch_to.frame(iframe_element)
time.sleep(2)

button = driver.find_element(By.XPATH, '/html/body/button')
button.click()
time.sleep(2)

print(f"Confirmation alert text ------------> {driver.switch_to.alert.text}")

# driver.switch_to.alert.accept()
# print("\nYou clicked Accept!")
# time.sleep(2)

driver.switch_to.alert.dismiss()
print("\nYou clicked cancel!")
time.sleep(2)

driver.switch_to.default_content()
time.sleep(2)

driver.quit()