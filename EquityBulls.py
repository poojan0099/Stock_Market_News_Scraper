from bs4 import BeautifulSoup
import requests


url = "https://www.equitybulls.com/"

news = requests.get(url)
doc = BeautifulSoup(news.text, "html.parser")

headings = []
for updates in doc.find_all("div", attrs={"class": "media-body"}):
    headings.append(updates.text)

#print("HEADINGS=", headings)


click_link = []
for l in doc.find_all(class_="catg_title", href=True):
    l_ck = l.get('href')
    click_link.append("https://www.equitybulls.com/" + l_ck)

#print("Links = ", click_link)

headings_links = dict(zip(headings, click_link))


if __name__ == "__main__":
    print(headings_links)

