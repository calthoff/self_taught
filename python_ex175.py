# IMPORTANT. I recently changed this example in the book.
# In older versions of the book the example was:

#name = "Walter Isaacson"
#year_born = "1952"
#book1 = "Steve Jobs"
#book2 = "Benjamin Franklin"

#"""{} was born in {}.
#   He's written books about
#   {} and {}.
#""".format(name, year_born,
#            book1, book2)

# I made this change so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


author = "William Faulkner"
year_born = "1897"

"""{} was born in {}."""\
   .format(author,
           year_born)