import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B01K1HPA60")

price_dollar = driver.find_element(By.CSS_SELECTOR, ".a-price-whole")
price_cents = driver.find_element(By.CSS_SELECTOR, ".a-price-fraction")
whole_price = (float(f"{price_dollar.text}.{price_cents.text}"))
print(whole_price)

my_email = "buzinov.yura@gmail.com"
subject = f"Subject:Time to buy Philips Trimmer ${whole_price} on Amazon"
body = f"Best price for this:\n{'https://www.amazon.com/dp/B01K1HPA60'}\nhttps://camelcamelcamel.com/product/B01K1HPA60"

if whole_price <= 20:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="lcgy eebc gcvp vmus")
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"{subject}\n\n{body}")


driver.quit()