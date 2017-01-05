import re


line = "123?34 hello?"


m = re.findall("\d",
               line,
               re.IGNORECASE)

print(m)
