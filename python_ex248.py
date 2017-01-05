# IMPORTANT. I changed many of the variable names in this example
# so the example fits on smaller devices. Old versions of the book have longer
# variable names. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)

