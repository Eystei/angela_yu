import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "123"
NEWS_API_KEY = "123"
TWILIO_SID = "123"
TWILIO_AUTH_TOKEN = "123"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# YESTERDAY CLOSING STOCK PRICE
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_data)

# DAY BEFORE YESTERDAY'S CLOSING PRICE
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_data)

# FIND THE POSITIVE DIFFERENCE BETWEEN 1 AND 2
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"

# PERCENTAGE DIFF BETWEEN CLOSING PRICE YESTERDAY & DAY_BEFORE_YESTERDAY
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)

# IF PERCENTAGE IS GREATER THAN 5 THEN PRINT("Get News")
if abs(diff_percent) > 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # LIST THAT CONTAINS THE FIRST THREE ARTICLES FROM NEWS
    three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percent}%" \
        f"\nHeadline: {article['title']}. " \
        f"\nBrief: {article['description']}" for article in three_articles]
    # print(formatted_articles)

    # SEND EACH ARTICLE AS A SEPARATE MESSAGE VIA TWILIO
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        print(article)
        # message = client.messages.create(
        #     body=article,
        #     from_="+123",
        #     to="+123"
        # )
