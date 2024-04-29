from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

events_dates = [f"{item.get_attribute('datetime')}".split("T")[0] for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
events_names = [item.text for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")]

event_dict = {}
for i in range(len(events_dates)):
    event_dict[i] = {
        "time": events_dates[i],
        "name": events_names[i]
    }

pprint(event_dict)



driver.quit()
