class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))

my_shape = Shape(20, 25)
my_shape.print_size()
