# I changed the variable in this example from
#  new_shows in older versions of the book to new 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!

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
