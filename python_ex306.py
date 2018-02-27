# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


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
