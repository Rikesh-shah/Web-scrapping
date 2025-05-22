import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target"
driver.get(url)
time.sleep(2)

# identify the iframe and switch into it
iframe_element = driver.find_element(By.XPATH, '//*[@id="iframeResult"]')
driver.switch_to.frame(iframe_element)

link = driver.find_element(By.XPATH, 'html/body/p[1]/a')
link.click()
time.sleep(2)

# switch back to default content
driver.switch_to.default_content()

driver.quit()