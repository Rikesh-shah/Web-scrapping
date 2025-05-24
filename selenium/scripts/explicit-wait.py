import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.google.com/"
driver.get(url)
time.sleep(2)

search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_bar.send_keys("Machine Learning")

wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')))

search_bar.send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()