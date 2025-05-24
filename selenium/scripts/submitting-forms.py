import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = 'https://github.com/login'
driver.get(url)
time.sleep(1)

# username field
username_field = driver.find_element(By.ID, 'login_field')
username_field.send_keys('rikesh')
time.sleep(1)

# password field
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('password')
time.sleep(1)

# submit button
submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
submit_button.click()
time.sleep(2)

driver.quit()