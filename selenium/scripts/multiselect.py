import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = uc.Chrome()
driver.maximize_window()

url = "https://demoqa.com/select-menu"
driver.get(url)
time.sleep(2)

cars_element = driver.find_element(By.XPATH, '//*[@id="cars"]')

cars_ms = Select(cars_element)

time.sleep(2)

cars_ms.select_by_index(1)
time.sleep(2)

cars_ms.select_by_visible_text("Opel")
time.sleep(1)

cars_ms.select_by_visible_text("Audi")
time.sleep(1)

# deselecting options

cars_ms.deselect_by_index(2)
time.sleep(1)

cars_ms.deselect_all()
time.sleep(3)

driver.quit()