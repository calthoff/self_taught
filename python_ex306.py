
def sequential_search(number_list,
                        number):
    found = False
    for i in number_list:
        if i == number:
            found = True
            break
    return found
nmbers = range(0, 100)
s1 = sequential_search(nmbers, 2)
print(s1)
s2 = sequential_search(nmbers, 202)
print(s2)
