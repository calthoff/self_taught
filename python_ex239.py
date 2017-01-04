def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    letters_left = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter")
        if guess in letters_left:
            cindex = letters_left.index(guess)
            board[cindex] = guess
            letters_left[cindex] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(stages[0: wrong + 1]))
        if "__" not in board:
            print("You win!"
                  .format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")