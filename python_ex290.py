def scrape(self):
    r = urllib.request\
        .urlopen(self.site)
    html = r.read()