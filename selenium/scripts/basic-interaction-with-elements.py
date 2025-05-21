import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.google.com"
driver.get(url)

search_bar_xpath = '//*[@id="APjFqb"]'
search_bar = driver.find_element(by = By.XPATH, value = search_bar_xpath)

# enter input
search_bar.send_keys("Machine Learning")
# time.sleep(1)

# clear input fields
# search_bar.clear()
# time.sleep(2)

# press enter key
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# clicking action
link_xpath = '//*[@id="rso"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/span/a/h3'
link = driver.find_element(by = By.XPATH, value = link_xpath)
link.click()
time.sleep(5)

driver.quit()