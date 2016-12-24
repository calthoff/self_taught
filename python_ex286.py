
# http://tinyurl.com/hwek4d3


import re


line = "I love $"


m = re.findall("\\$",
                     line,
                     re.IGNORECASE)


print(m)
