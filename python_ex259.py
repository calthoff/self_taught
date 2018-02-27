# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
             """.format(self.width,
                        self.len))


class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()
