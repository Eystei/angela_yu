from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news?p=1")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(".titleline a[href*='https']")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes_int = [int(score.getText().split(" ")[0]) for score in soup.select("span .score")]


max_upvote = article_upvotes_int.index(max(article_upvotes_int))

print(article_texts[max_upvote])
print(article_links[max_upvote])
print(f"points {article_upvotes_int[max_upvote]}")




