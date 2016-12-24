
# http://tinyurl.com/gvajo3x


import re




text = "__one__ __two__ __three__"


results = re.findall("__.*?__", text)


for match in results:
    print(match)
