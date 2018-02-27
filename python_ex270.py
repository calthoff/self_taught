# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)
