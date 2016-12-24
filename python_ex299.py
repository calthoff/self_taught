
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
        return self.items[len(self.items)-1]


    def size(self):
        return len(self.items)


stack = Stack()
for c in "Hello":
    stack.push(c)


reversed_string = ""


for i in range(len(stack.items)):
    reversed_string += stack.pop()


print(reversed_string)
