
# http://tinyurl.com/ztysa6b


import urllib.request
from bs4 import BeautifulSoup




class Scraper:
    def __init__(self, site):
        self.site = site


    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("a"):
            url = tag.get("href")
            if url and "html" in url:
                print("\n" + url)


url = "https://news.google.com/"
Scraper(url).scrape()
