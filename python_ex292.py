
def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("a"):
        url = tag.get("href")
        if url and "html" in url:
            print("\n" + url)
