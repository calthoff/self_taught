# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). Keep up the hard work!



def scrape(self):
    r = urllib.request\
        .urlopen(self.site)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html,
                       parser)

