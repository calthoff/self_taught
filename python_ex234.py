# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


import csv


with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one",
                    "two",
                    "three"])
    write.writerow(["four",
                    "five",
                    "six"])
