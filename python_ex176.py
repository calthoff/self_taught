# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.

n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(n1,
               v,
               adj,
               n2)

print(r)
