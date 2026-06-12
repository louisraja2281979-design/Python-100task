from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configure Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

search_query = "restaurants in Chennai"
url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"

driver.get(url)
time.sleep(5)

# Scroll to load more results
scrollable_div = driver.find_element(
    By.XPATH,
    '//div[@role="feed"]'
)

for _ in range(10):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        scrollable_div
    )
    time.sleep(2)

businesses = driver.find_elements(
    By.CSS_SELECTOR,
    'div[role="article"]'
)

data = []

for business in businesses:
    try:
        name = business.find_element(
            By.CSS_SELECTOR,
            '.fontHeadlineSmall'
        ).text
    except:
        name = ""

    try:
        rating = business.find_element(
            By.CSS_SELECTOR,
            '.fontBodyMedium span[role="img"]'
        ).get_attribute("aria-label")
    except:
        rating = ""

    try:
        address = business.text
    except:
        address = ""

    data.append({
        "Name": name,
        "Rating": rating,
        "Address": address
    })

df = pd.DataFrame(data)
df.to_csv("google_maps_results.csv", index=False)

print(f"Saved {len(df)} records to google_maps_results.csv")

driver.quit()