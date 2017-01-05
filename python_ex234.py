# IMPORTANT. In some previous versions of the book, this example contains an error.
# I've fixed the error in the newest version of the book and it is fixed below. "new_file.csv" should be
# "st.csv"
# If you have an older version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


import csv


with open("st.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one",
                    "two",
                    "three"])
    write.writerow(["four",
                    "five",
                    "six"])
