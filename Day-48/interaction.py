import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# ------------------------------------------- STILL TO BE COMPLETED ----------------------------------------------------


# ------------------------------------------- WIKIPEDIA PAGE ----------------------------------------------------
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
#
# no_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
# print(no_of_articles)


# ------------------------------------------- SIGN UP PAGE ----------------------------------------------------
# driver.get(url="https://secure-retreat-92358.herokuapp.com/")
# f_name = driver.find_element(By.NAME, value='fName')
# f_name.send_keys("lolfname")
# l_name = driver.find_element(By.NAME, value='lName')
# l_name.send_keys("lollname")
# email = driver.find_element(By.NAME, value='email')
# email.send_keys("lolemail@lolmail.com")
#
# driver.find_element(By.XPATH, value='/html/body/form/button').click()


# ------------------------------------------- COOKIE CLICEKR ----------------------------------------------------
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
keep_clicking = True
timeout = time.time() + 5

available_purchases_dict = {}

available_items = driver.find_element(By.ID, value='//*[@id="buyCursor"]').text
for item in range(0, 8):
    all_prices = driver.find_element(By.CSS_SELECTOR, value='#store b')
    print(all_prices)
    available_purchases_dict = {
        "item_name":"",
        "item_price":""
    }

def check_for_purchase():
    available_coins = driver.find_element(By.XPATH, value='//*[@id="money"]').text
    print(available_coins)

    available_items = driver.find_element(By.ID, value='store').text
    # for item in available_items:
        # Buy most expensive item

    print(available_items)

def check_time():
    global timeout
    if time.time() > timeout:
        check_for_purchase()
        time.time() + 5
        timeout = time.time() + 5

cookie_photo = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

while keep_clicking:
    check_time()
    cookie_photo.click()