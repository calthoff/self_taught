
# http://tinyurl.com/ztolacl


from random import shuffle


class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    values = [None, None,"2", "3",
             "4", "5", "6", "7", "8",
             "9", "10", "Jack",
             "Queen", "King",
             "Ace"]

    def __init__(self, value, suit):
        """suit and value are ints"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] \
            + " of " + self.suits[self.suit]
        return v


class Deck:
   def __init__(self):
       self.cards = []
       for i in range(2, 15):
           for j in range(4):
               self.cards.append(Card(i, j))
       shuffle(self.cards)

   def rm_card(self):
       if len(self.cards) == 0:
           return
       return self.cards.pop()


class Player:
   def __init__(self, name):
       self.wins = 0
       self.card = None
       self.name = name


class Game:
   def __init__(self):
       name1 = input("p1 name ")
       name2 = input("p2 name ")
       self.deck = Deck()
       self.p1 = Player(name1)
       self.p2 = Player(name2)

   def play_game(self):
       cards = self.deck.cards
       print("beginning War!")
       response = None
       while len(cards) >= 2:
           response = input("""q to
                            quit. other
                            key to
                            play.""")
           if response == 'q':
               break
           p1_card = self.deck.rm_card()
           p2_card = self.deck.rm_card()
           print("""{} drew {} {} drew {}
           """.format(self.p1.name,
                      p1_card,
                      self.p2.name,
                       p2_card))
           if p1_card > p2_card:
               self.p1.wins += 1
               print("""{} wins this round
                     """.format(self.p1.name))
           else:
               self.p2.wins += 1
               print("""{} wins this round
          """.format(self.p2.name))
       print("""The War is over.{} wins
        """.format(self.winner(self.p1,
                               self.p2)))

   def winner(self, p1, p2):
       if p1.wins > p2.wins:
           return p1.name
       if p1.wins < p2.wins:
           return p2.name
       return "It was a tie!"


game = Game()
game.play_game()
