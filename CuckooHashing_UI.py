class CuckooHashing:
    def __init__(self, size=11):
        self.size = size
        self.t1 = [None] * size
        self.t2 = [None] * size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return (key // self.size) % self.size

    def _place(self, key):
        current = key
        table_no = 1

        for _ in range(2 * self.size):
            if table_no == 1:
                table, index = self.t1, self.h1(current)
            else:
                table, index = self.t2, self.h2(current)

            if table[index] is None:
                table[index] = current
                return True

            table[index], current = current, table[index]
            table_no = 2 if table_no == 1 else 1

        return False

    def insert(self, key):
        if self.search(key):
            return True

        old1, old2 = self.t1[:], self.t2[:]
        keys = [x for x in self.t1 + self.t2 if x is not None]
        keys.append(key)

        if self._place(key):
            return True

        self.t1, self.t2 = old1, old2

        for _ in range(10):
            self.size = self.size * 2 + 1
            self.t1 = [None] * self.size
            self.t2 = [None] * self.size

            if all(self._place(x) for x in keys):
                return True

        # Restore the previous table if all attempts fail.
        self.size = len(old1)
        self.t1, self.t2 = old1, old2
        return False

    def search(self, key):
        return (self.t1[self.h1(key)] == key or
                self.t2[self.h2(key)] == key)

    def delete(self, key):
        i = self.h1(key)
        if self.t1[i] == key:
            self.t1[i] = None
            return True

        i = self.h2(key)
        if self.t2[i] == key:
            self.t2[i] = None
            return True

        return False

    def display(self):
        print("Table 1:", self.t1)
        print("Table 2:", self.t2)


if __name__ == "__main__":
    cuckoo = CuckooHashing()

    n = int(input("Enter number of keys: "))
    keys = list(map(
        int, input("Enter keys separated by spaces: ").split()
    ))

    if n < 0 or len(keys) != n:
        print("Invalid input")
    else:
        for key in keys:
            if not cuckoo.insert(key):
                print("Insertion failed:", key)

        cuckoo.display()

        x = int(input("Enter key to search: "))
        print("Found" if cuckoo.search(x) else "Not found")

        x = int(input("Enter key to delete: "))
        print("Deleted" if cuckoo.delete(x) else "Key not found")

        cuckoo.display()