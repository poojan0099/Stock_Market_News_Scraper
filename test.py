from bs4 import BeautifulSoup
import requests

url = "https://www.livemint.com/market/stock-market-news"

news = requests.get(url)
doc = BeautifulSoup(news.text, "html.parser")

headings = doc.find()