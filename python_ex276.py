# I split the line of code self.cards.append(Card(i, j)) in early versions of the book into two lines:
# self.cards\
# .append(Card(i,
#              j))
# Email cory@theselftaughtprogrammer.io for latest version


from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
