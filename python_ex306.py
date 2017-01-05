# I changed the variable in this example from
#  number in older versions of the book to n 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)
