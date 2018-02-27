# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request\
            .urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,
                           parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()

