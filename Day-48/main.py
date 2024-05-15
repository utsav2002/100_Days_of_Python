from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.co.uk/Wrangler-Authentics-Classic-Relaxed-Stonewash/dp/B00XKXTVCC/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=8z10e&content-id=amzn1.sym.6aea875e-359f-49f3-864f-cff62d586b6a%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=6aea875e-359f-49f3-864f-cff62d586b6a&pf_rd_r=DW1GA9VWCN01PHFGVKYW&pd_rd_wg=xBYBo&pd_rd_r=4890c02a-d332-4434-8c59-5aa1c8b43472&pd_rd_i=B00XKXTVCC&th=1&psc=1"
PYTHON_DOCUMENTATION_URL = "https://www.python.org/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_DOCUMENTATION_URL)
# price_of_product = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]').text
# print(price_of_product)

upcoming_event = {}

for event in range(1, 6):
    event_date = (driver.find_element(By.XPATH,
                                      value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{event}]/time')).text
    event_name = (
        driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{event}]/a')).text

    upcoming_event[event] = {
        "Time": event_date,
        "Name": event_name
    }

print(upcoming_event)

driver.quit()
