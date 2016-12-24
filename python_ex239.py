
 # http://tinyurl.com/hshb567


def hangman(word):
    wrong = 0
   stages = ["",
             "________
             ",
             "|      |      ",
             "|      0
          ", "|     /|\     ",
             "|     / \     ",
             "|
            "]




    letters_left = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter")
        if guess in letters_left:
            cindex = letters_left.index(guess)
            letter_board[cindex] = guess
            letters_left[cindex] = '$'
        else:
            wrong += 1
        print((" ".join(letter_board)))
        print("\n".join(stages[0: wrong + 1]))
        if "__" not in letter_board:
            print("You win! The word was:")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("""You lose!
     The words
     was {}""".format(word))


hangman("cat")
