# I changed the variable in this example from
#  length in older versions of the book to len 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l


    def area(self):
        return self.width * self.len