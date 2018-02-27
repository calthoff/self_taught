# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


import csv


# make sure you’ve created
# the file from the previous
# example


with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
