from bs4 import BeautifulSoup
import requests
import re

url = "https://www.livemint.com/market/stock-market-news"

news = requests.get(url)
doc = BeautifulSoup(news.text, "html.parser")

headings_links_html = doc.select(".headline")
print(headings_links_html)

headings = [updates.text.strip() for updates in headings_links_html]

print(headings)

click_link = list()
for l in doc.find_all("h2", attrs={"class": "headline"}, href=True):
    if l.get('href').endswith('html'):
        click_link.append(l.get('href'))


print(click_link)