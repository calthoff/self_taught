# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }


n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")
