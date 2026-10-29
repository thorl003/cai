import threading

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ConcurrentLinkedList:
    def __init__(self):
        self.head = None
        self.lock = threading.RLock()

    def append(self, data):
        new = Node(data)
        with self.lock:
            if not self.head:
                self.head = new
                return
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new

    def prepend(self, data):
        with self.lock:
            new = Node(data)
            new.next = self.head
            self.head = new

    def delete(self, data):
        with self.lock:
            cur = self.head
            if not cur:
                return False
            if cur.data == data:
                self.head = cur.next
                return True
            while cur.next:
                if cur.next.data == data:
                    cur.next = cur.next.next
                    return True
                cur = cur.next
            return False

    def contains(self, data):
        with self.lock:
            cur = self.head
            while cur:
                if cur.data == data:
                    return True
                cur = cur.next
            return False

    def display(self):
        with self.lock:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
            print()

def add_items(ll, values):
    for x in values:
        ll.append(x)

ll = ConcurrentLinkedList()

values = list(map(int, input("Enter values: ").split()))

t1 = threading.Thread(target=add_items, args=(ll, values[::2]))
t2 = threading.Thread(target=add_items, args=(ll, values[1::2]))

t1.start()
t2.start()
t1.join()
t2.join()

print("Linked List:")
ll.display()

x = int(input("Enter value to prepend: "))
ll.prepend(x)
print("After Prepend:")
ll.display()

x = int(input("Enter value to delete: "))
print("Deleted:", ll.delete(x))
print("After Delete:")
ll.display()

x = int(input("Enter value to search: "))
print("Found:", ll.contains(x))