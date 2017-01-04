# I shortened the message that gets printed in this example.
# The example in older versions of the book prints "Type another number:"
# I did this so the example will fit better on smaller devices.
# If you have an older version of the book, you can email
# me at cory@theselftaughtprogrammer.io 
# to update to the newest version. Thank you so much for purchasing my book!


a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")
