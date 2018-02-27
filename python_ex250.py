# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


class Orange():
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
