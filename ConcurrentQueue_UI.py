import threading
from collections import deque

class ConcurrentQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, x):
        with self.lock:
            self.queue.append(x)

    def dequeue(self):
        with self.lock:
            return self.queue.popleft() if self.queue else "Queue Empty"

    def display(self):
        with self.lock:
            print(list(self.queue))

def add_items(q, values):
    for x in values:
        q.enqueue(x)

q = ConcurrentQueue()

values = list(map(int, input("Enter queue values: ").split()))

t1 = threading.Thread(target=add_items, args=(q, values[::2]))
t2 = threading.Thread(target=add_items, args=(q, values[1::2]))

t1.start()
t2.start()
t1.join()
t2.join()

print("Queue:")
q.display()

print("Dequeued:", q.dequeue())
print("After Dequeue:")
q.display()