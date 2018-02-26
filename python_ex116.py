# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
