# I changed the variable in this example from
#  read or reader in older versions of the book to r 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!



import csv


# make sure you’ve created
# the file from the previous
# example


with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
