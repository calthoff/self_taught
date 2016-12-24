
# http://tinyurl.com/goqtw53


class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l


    def print_size(self):
        print("""{} by {}
         """.format(self.width,
         self.length))




 class Square(Shape):
    def area(self):
        return self.width * self.length


    def print_size(self):
        print("""I am a square
        that is {} by {}"""
        .format(self.width,
                self.length))


a_square = Square(20, 20)
a_square.print_size()
