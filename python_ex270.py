
# http://tinyurl.com/gv7zwjx


class Person:
    def __init__(self):
        self.name = 'Bob'


bob = Person()
the_same_bob = bob
print(bob is the_same_bob)


another_bob = Person()
print(bob is another_bob)
