
# http://tinyurl.com/jpqahfb


import csv


# make sure you’ve created
# the file from the previous
# example


with open("st.csv", "r") as f:
    rder = csv.reader(f, delimiter=",")
    for row in rder:
        print(",".join(row))
