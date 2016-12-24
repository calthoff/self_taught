
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
                            quit. Other
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
