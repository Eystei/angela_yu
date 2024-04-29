from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import time

google_form_link = "https://forms.gle/jhEKaGCz6vA5urTP7"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,de;q=0.6"
}

response = requests.get(
    "https://www.list.am/ru/category/56?cmtype=1&type=1&n=8&price1=&price2=1000&crc=1&_a5=0&_a39=0&_a40=0&_a85=0&_a73=0&_a3_1=&_a3_2=&_a4=2&_a37=0&_a36=0&_a11_1=&_a11_2=&_a41=0&_a78=0&_a38=0&_a74=0&_a75=0&_a77=0&_a68=0&_a69=0",
    headers=header)

site_html = response.text
soup = BeautifulSoup(site_html, "html.parser")

all_links = [f"https://www.list.am{item['href']}" for item in soup.select(".dl .gl a")]
all_text = [item.text for item in soup.select(".dl .gl a .l")]
all_prices = [item.text for item in soup.select(".dl .gl .p")]

for i in range(len(all_links)):
    print(all_prices[i], all_text[i], all_links[i])

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get(google_form_link)

for i in range(len(all_links)):
    time.sleep(1 / 2)
    text_element = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i1"]')
    text_element.send_keys(all_text[i])

    price_element = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i5"]')
    price_element.send_keys(all_prices[i])

    link_element = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i9"]')
    link_element.send_keys(all_links[i])

    button_element = driver.find_element(By.XPATH, "//span[text()='Отправить']")
    button_element.click()

    another_one_element = driver.find_element(By.CSS_SELECTOR, '[href*="form_confirm"]')
    another_one_element.click()

print(f"Number of Items: {len(all_links)}")