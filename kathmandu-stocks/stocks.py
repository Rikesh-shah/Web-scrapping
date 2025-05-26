import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()

# explicit wait
wait = WebDriverWait(driver, 2)

url = "https://nepalbhoomi.com/"
driver.get(url)
# driver.save_screenshot('screenshot.png')
time.sleep(2)

# hovering on buy option
actions = ActionChains(driver)
buy_menu = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]'))
)
actions.move_to_element(buy_menu).perform()

# click on house
house = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]/p[1]'))
)
house.click()


data = []
page_count = 0
while True:
	page_count += 1
	# click next
	try:
		next_button = wait.until(
			EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]"))
		)
	except:
		print("The \"next\" button is not clickable. We have navigated through all the pages.")
		print(f"Timeout because we have navigated all the {page_count} pages.\n")
		break
	else:
		try:

			driver.execute_script("window.scrollBy(0, arguments[0].getBoundingClientRect().top - 100);", next_button)
			time.sleep(1)

			# scraping the data
			rows = driver.find_elements(By.CLASS_NAME, "item.important")

			for row in rows:
				#property name
				try:
					name = row.find_element(By.CLASS_NAME, "property_name_here").text
				except:
					name = np.nan

				# property location
				try:
					location_span = row.find_element(By.XPATH, ".//span[@title]")
					location = location_span.get_attribute("title")
				except:
					location = np.nan

				# property price
				try:
					price = row.find_element(By.CLASS_NAME, "property_prices").text
				except:
					price = np.nan

				property = {
					"name" : name,
					"location" : location,
					"price" : price
				}
				data.append(property)

			wait.until(
					EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]"))
				).click()
			time.sleep(2)
		except:
			print("Timeout while clicking on \"Next Page\".\n")

# scraping data from the last page
rows = driver.find_elements(By.CLASS_NAME, "item.important")

for row in rows:
	#property name
	try:
		name = row.find_element(By.CLASS_NAME, "property_name_here").text
	except:
		name = np.nan

	# property location
	try:
		location_span = row.find_element(By.XPATH, ".//span[@title]")
		location = location_span.get_attribute("title")
	except:
		location = np.nan

	# property price
	try:
		price = row.find_element(By.CLASS_NAME, "property_prices").text
	except:
		price = np.nan

	property = {
		"name" : name,
		"location" : location,
		"price" : price
	}
	data.append(property)

time.sleep(2)
driver.quit()

# ==================== Cleaning the Data ==================== #
def clean_price(val):
    if pd.isna(val):
        return None
    val = str(val).replace("npr.", "").strip()
    if "cr" in val:
        return float(val.replace("cr", "").replace(",", "").strip()) * 1e7
    else:
        return float(val.replace(",", "").strip())
	

df_properties = (
	pd
	.DataFrame(data)
	.drop_duplicates()
	.apply(lambda col : col.str.strip().str.lower() if col.dtype == "object" else col)
	.assign(
		price = lambda df_ : (
			df_
			.price
			.str.replace('NPR\.\s*', '', regex=True)
			.apply(clean_price)
		)
	)
	.reset_index(drop=True)
	.to_csv("Kathmandu.csv", index = False)
)
# property_df = pd.DataFrame(data)
# property_df.to_csv("Kathmandu.csv", index = False)