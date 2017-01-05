# I changed the variable in this example from
#  text in older versions of the book to t 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


import re


t = "__one__ __two__ __three__"


results = re.findall("__.*?__", t)


for match in results:
    print(match)
