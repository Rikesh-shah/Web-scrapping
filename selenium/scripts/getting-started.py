from selenium import webdriver
import time

# initialize the chrome driver
driver = webdriver.Chrome()

# delay for 5 seconds to allow the page to load
time.sleep(2)

driver.maximize_window()

time.sleep(2)

url = "https://www.google.com"
driver.get(url)

# printing meta-data of webpage
print(f"Title: {driver.title}")
print(f"Current URL: {driver.current_url}")

# capture screenshot of webpage
driver.save_screenshot("google-screenshot.png")
print("\nscreenshot taken!")

time.sleep(1)

# close the browser window
driver.quit()