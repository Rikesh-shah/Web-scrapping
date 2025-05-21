import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

url = "https://www.google.com/"
driver.get(url)
time.sleep(2)

search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_bar.send_keys("Machine Learning")

search_bar.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()