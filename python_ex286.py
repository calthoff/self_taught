import re


line = "I love $"


m = re.findall("\\$",
               line,
               re.IGNORECASE)

print(m)
