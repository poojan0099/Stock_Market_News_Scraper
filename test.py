from bs4 import BeautifulSoup
import requests


url = "https://www.equitybulls.com/"

news = requests.get(url)
doc = BeautifulSoup(news.text, "html.parser")

print(news)