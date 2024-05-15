import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINKEDIN_URL = "https://www.linkedin.com/login"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=LINKEDIN_URL)

# Log in
email_input = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_input.send_keys("utsavkothari2002@gmail.com")
pass_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
pass_input.send_keys("MseZyx8/.9,83Re")
driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()

# Input all details
search_box = driver.find_element(By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
search_box.send_keys("Machine Learning Engineer")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[2]/button').click()
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="ember745"]').click()

#  Reached certain point, only remaining part is to apply with the phone number, rest is done!
