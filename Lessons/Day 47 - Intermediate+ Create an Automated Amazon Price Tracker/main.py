import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/gp/product/B01K1HPA60/"
headers = {
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,de;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
amazon_html = response.text
# print(amazon_html)


soup = BeautifulSoup(amazon_html, "html.parser")
price_element = soup.select('p span .green')[0]
price_as_float = float(price_element.getText().split("$")[1])
print(price_as_float)

my_email = "buzinov.yura@gmail.com"
subject = f"Subject:Time to buy Philips Trimmer ${price_as_float} on Amazon"
body = f"Best price for this:\n\n{url}"

if price_as_float <= 20:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="lcgy **** gcvp vmus")
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"{subject}\n\n{body}")
