# IMPORTANT. I changed the way this example works
# so it will fit on smaller devices. Old versions of the book have
# a different example. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!

while wrong < len(stages) - 1:
    print("\n")
    msg = "Guess a letter"
    char = input(msg)
    if char in rletters:
        cind = rletters \
               .index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
    print((" ".join(board)))
    e = wrong + 1
    print("\n"
          .join(stages[0: e]))
    if "__" not in board:
        print("You win!")
        print(" ".join(board))
        win = True
        break
