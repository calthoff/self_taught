
# http://tinyurl.com/hshb567


def hangman(word):
    wrong = 0
    stages = ["",
             "________",
             "",
             "|      |      ",
             "|      0      ",
             "|     /|\     ",
             "|     / \     ",
             "|"             ,
             ]
    letters_left = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')

hangman("hello")
