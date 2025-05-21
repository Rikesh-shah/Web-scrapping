import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.miniclip.com/careers/vacancies"
driver.get(url)
time.sleep(2)

# identify the department
departments_field = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/section[2]/div/fieldset[3]/select')

# convert to drop down element
departments_dropdown = Select(departments_field)
time.sleep(2)

departments_dropdown.select_by_index(4)
time.sleep(5)

departments_dropdown.select_by_visible_text("Player Support")
time.sleep(2)