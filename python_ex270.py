# variable name the_same_bob in older editions of the book changed to same_bob.
# Email cory@theselftaughtprogrammer.io for latest version


class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)
