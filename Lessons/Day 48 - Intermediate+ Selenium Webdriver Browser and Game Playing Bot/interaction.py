from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("headless=new")

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count_article = driver.find_element(By.CSS_SELECTOR, "[title='Special:Statistics']")
print(count_article.text)

search = driver.find_element(By.CSS_SELECTOR, "#searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)