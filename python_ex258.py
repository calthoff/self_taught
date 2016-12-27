
# http://tinyurl.com/h7zmz6f


class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("""{} by {}
        """.format(self.width,
                  self.length))


my_shape = Shape(20, 25)
my_shape.print_size()
