# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n +
                   other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
