
# http://tinyurl.com/jg86ndz


import re


line = "Beautiful is better than ugly."


matches = re.findall("beautiful", line, re.IGNORECASE)


print(matches)
