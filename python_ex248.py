
# http://tinyurl.com/jgugkao


class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        print("""Orange object
                created!""")


or1 = Orange(10, "dark orange")


or1.weight = 100
or1.color = "light orange"


print(or1.weight)
print(or1.color)
