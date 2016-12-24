
# http://tinyurl.com/hms5wr4


import re


string = "Two too."


m = re.findall("t[ow]o",
          string,
          re.IGNORECASE)
print(m)
