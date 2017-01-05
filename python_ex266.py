# variable name length in older editions of the book changed to len.
# Also the variable name created was changed to recs.
# Email cory@theselftaughtprogrammer.io for latest version


class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,
                          self.len))

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

