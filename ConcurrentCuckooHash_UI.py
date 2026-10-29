import threading
import hashlib


class CuckooHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table1 = [None] * size
        self.table2 = [None] * size
        self.lock = threading.RLock()

    def _hash(self, key, salt):
        data = f"{salt}:{key}".encode()
        value = int.from_bytes(
            hashlib.sha256(data).digest()[:8], "big"
        )
        return value % self.size

    def h1(self, key):
        return self._hash(key, "first")

    def h2(self, key):
        return self._hash(key, "second")

    def _items(self):
        return [
            key for key in self.table1 + self.table2
            if key is not None
        ]

    def _place(self, key):
        current = key
        table_no = 1
        seen = set()

        for _ in range(2 * self.size):
            state = (current, table_no)

            if state in seen:
                return False
            seen.add(state)

            if table_no == 1:
                index = self.h1(current)
                table = self.table1
            else:
                index = self.h2(current)
                table = self.table2

            if table[index] is None:
                table[index] = current
                return True

            table[index], current = current, table[index]
            table_no = 2 if table_no == 1 else 1

        return False

    def insert(self, key):
        with self.lock:
            if self.search(key):
                return True

            old1 = self.table1[:]
            old2 = self.table2[:]
            old_size = self.size

            if self._place(key):
                return True

            self.table1 = old1
            self.table2 = old2
            items = self._items() + [key]
            new_size = old_size

            for _ in range(20):
                new_size = new_size * 2 + 1
                self.size = new_size
                self.table1 = [None] * new_size
                self.table2 = [None] * new_size

                if all(self._place(item) for item in items):
                    return True

            self.size = old_size
            self.table1 = old1
            self.table2 = old2
            return False

    def search(self, key):
        with self.lock:
            return (
                self.table1[self.h1(key)] == key
                or self.table2[self.h2(key)] == key
            )

    def delete(self, key):
        with self.lock:
            i = self.h1(key)
            if self.table1[i] == key:
                self.table1[i] = None
                return True

            i = self.h2(key)
            if self.table2[i] == key:
                self.table2[i] = None
                return True

            return False

    def display(self):
        with self.lock:
            print("Table 1:", self.table1)
            print("Table 2:", self.table2)
            print("Capacity:", self.size)


def worker(table, keys):
    for key in keys:
        if not table.insert(key):
            print("Insertion failed:", key)


if __name__ == "__main__":
    cuckoo = CuckooHashTable()

    n = int(input("Enter number of keys: "))
    keys = list(map(
        int, input("Enter keys separated by spaces: ").split()
    ))

    if n < 0 or len(keys) != n:
        print("Invalid input: enter exactly n keys.")
    else:
        # Divide keys between two threads.
        t1 = threading.Thread(
            target=worker, args=(cuckoo, keys[::2])
        )
        t2 = threading.Thread(
            target=worker, args=(cuckoo, keys[1::2])
        )

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        cuckoo.display()

        x = int(input("Enter key to search: "))
        print("Found" if cuckoo.search(x) else "Not found")

        x = int(input("Enter key to delete: "))
        print("Deleted" if cuckoo.delete(x) else "Key not found")

        cuckoo.display()
