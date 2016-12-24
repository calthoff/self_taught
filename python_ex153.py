
# http://tinyurl.com/h7e7oz4


rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor"
          "5": "live"
          }


n = input("Type a number:")
if n in songs:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Couldn’t find it.")
