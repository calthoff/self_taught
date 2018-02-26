# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io with any questions.


a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")
