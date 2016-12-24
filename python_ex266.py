
# http://tinyurl.com/jth53yt


class Rectangle():
    created = []


    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.created.append((self.width,
                             self.length))


    def print_size(self):
        print("""{} by
        {}"""".format(self.width,
                      self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)


print(Rectangle.created)
