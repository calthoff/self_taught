
a_queue = Queue()


for i in range(5):
    a_queue.enqueue(i)


for i in range(5):
    print(a_queue.dequeue())


print()


print(a_queue.size())
