
# http://tinyurl.com/j6rgcov


class Orange():
    def __init__(self):
        """weights are in oz"""
        self.weight = 6
        self.color = 'orange'
        self.mold = 0


    def rot(self, days, temp):
        self.mold = days * (temp * .1)


orange = Orange()
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
