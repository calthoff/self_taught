# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). https://www.amazon.com/dp/B01M01YDQA#customerReviews. Keep up the hard work!


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
for c in "Hello":
    stack.push(c)


reversed_string = ""


for i in range(len(stack.items)):
    reversed_string += stack.pop()


print(reversed_string)
