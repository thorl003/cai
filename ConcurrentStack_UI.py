import threading

class ConcurrentStack:
    def __init__(self):
        self.stack = []
        self.lock = threading.Lock()

    def push(self, x):
        with self.lock:
            self.stack.append(x)

    def pop(self):
        with self.lock:
            return self.stack.pop() if self.stack else "Stack Empty"

    def display(self):
        with self.lock:
            print(self.stack)

def push_items(s, values):
    for x in values:
        s.push(x)

s = ConcurrentStack()

values = list(map(int, input("Enter stack values: ").split()))

t1 = threading.Thread(target=push_items, args=(s, values[::2]))
t2 = threading.Thread(target=push_items, args=(s, values[1::2]))

t1.start()
t2.start()
t1.join()
t2.join()

print("Stack:")
s.display()

print("Popped:", s.pop())
print("After Pop:")
s.display()