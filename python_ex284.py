# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). Keep up the hard work!



import re


t = "__one__ __two__ __three__"


results = re.findall("__.*?__", t)


for match in results:
    print(match)
