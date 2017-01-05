# I shortened this example.
# The example in older versions of the book prints "Type another number:"
# I did this so the example will fit better on smaller devices.
# If you have an older version of the book, you can email
# me at cory@theselftaughtprogrammer.io 
# to update to the newest version. Thank you so much for purchasing my book!

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
