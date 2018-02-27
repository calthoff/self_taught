# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.

tv = ["GOT",
     "Narcos",
     "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1


print(tv)
