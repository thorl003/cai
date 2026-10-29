import heapq
from itertools import count

class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def huffman_coding(frequencies):
    counter = count()
    heap = []

    for symbol, frequency in frequencies.items():
        node = Node(symbol, frequency)
        heapq.heappush(
            heap, (frequency, next(counter), node)
        )

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        parent = Node(None, f1 + f2)
        parent.left = left
        parent.right = right

        heapq.heappush(
            heap, (parent.frequency, next(counter), parent)
        )

    root = heap[0][2]
    codes = {}

    def generate_codes(node, code):
        if node is None:
            return

        if node.symbol is not None:
            codes[node.symbol] = code if code else "0"
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")
    return codes

if __name__ == "__main__":
    n = int(input("Enter number of symbols: "))

    if n < 1:
        print("Number of symbols must be at least 1.")
        raise SystemExit

    frequencies = {}

    for i in range(n):
        symbol = input(f"Enter symbol {i + 1}: ")

        if len(symbol) != 1 or symbol in frequencies:
            print("Enter a unique, single-character symbol.")
            raise SystemExit

        frequency = int(input(f"Enter frequency of {symbol}: "))

        if frequency <= 0:
            print("Frequency must be positive.")
            raise SystemExit

        frequencies[symbol] = frequency

    codes = huffman_coding(frequencies)

    print("\nSymbol  Frequency  Huffman Code")
    for symbol, frequency in frequencies.items():
        print(f"{symbol:<8}{frequency:<11}{codes[symbol]}")