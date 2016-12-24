
# http://tinyurl.com/gl2kr4y


import csv


with open("new_file.csv",
     "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["one",
                    "two",
                    "three"])
    writer.writerow(["four",
                    "five",
                    "six"])
