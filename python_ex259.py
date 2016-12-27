
# http://tinyurl.com/h9zxkqd


class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l


    def print_size(self):
        print("""{} by {}
              """.format(self.width,
              self.length))


class Square(Shape):
    pass


a_square = Square(20,20)
a_square.print_size()
