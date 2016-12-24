
import time
import random




class Queue:
   def __init__(self):
       self.items = []


   def is_empty(self):
       return self.items == []


   def enqueue(self, item):
       self.items.insert(0, item)


   def dequeue(self):
       return self.items.pop()


   def size(self):
       return len(self.items)




def simulate_line(time_till_show,
                             max_time):
   pq = Queue()
   tickets_sold_to = []


   for i in range(100):
       pq.enqueue("person" + str(i))


   t_end = time.time() + time_till_show
   time = time.time()
   while time < t_end and not pq.is_empty():
       r = random.randint(0, max_time)
       time.sleep(r)
       tickets_sold_to.append(pq.dequeue())
   return tickets_sold_to[m][n]


print(simulate_line(5, 2))
