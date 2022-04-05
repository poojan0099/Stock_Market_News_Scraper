from bs4 import BeautifulSoup
import requests
from threading import Thread
import functools


def timeoutDecorator(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (
                func.__name__, timeout))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as e:
                print('error starting thread')
            ret = res[0]
            if isinstance(ret, BaseException):
                print("timeout occured ...")
                return ret
            return ret
        return wrapper
    return deco


def withTimeout(max_time):
    @timeoutDecorator(max_time)
    def inner(func, *args, **kwargs):
        return func(*args, **kwargs)
    return inner


def getHeadingLinksWrapper(url: str) -> dict:    
    news = requests.get(url)
    doc = BeautifulSoup(news.text, "html.parser")

    headings = []
    for updates in doc.find_all("div", attrs={"class": "media-body"}):
        headings.append(updates.text)

    click_link = []
    for l in doc.find_all(class_="catg_title", href=True):
        l_ck = l.get('href')
        click_link.append(url + l_ck)

    headings_links = dict(zip(headings, click_link))
    return headings_links


def getWithTimeout(url, timeout):
    print({
        "url": url,
        "timeout": timeout
    })
    timeoutFunction = withTimeout(timeout)
    return timeoutFunction(getHeadingLinksWrapper, url=url)
    
    
if __name__ == "__main__":
    equitybullURL = "https://www.equitybulls.com/"
    getWithTimeout(url=equitybullURL)
