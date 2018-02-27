# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). Keep up the hard work!


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

