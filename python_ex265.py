# variable name length in older editions of the book changed to len.
# Email cory@theselftaughtprogrammer.io for latest version


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.length))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()
