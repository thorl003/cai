def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()

    print("\nDP Table:")
    for row in dp:
        print(*row)

    print("\nMaximum Value:", dp[n][capacity])
    print("Selected Items (item number, weight, value):")

    for i in selected:
        print(i + 1, weights[i], values[i])


if __name__ == "__main__":
    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be positive.")
        raise SystemExit

    weights = []
    values = []

    for i in range(n):
        weight = int(input(f"Enter weight of item {i + 1}: "))
        value = int(input(f"Enter value of item {i + 1}: "))

        if weight <= 0 or value < 0:
            print("Weights must be positive and values non-negative.")
            raise SystemExit

        weights.append(weight)
        values.append(value)

    capacity = int(input("Enter knapsack capacity: "))

    if capacity < 0:
        print("Capacity cannot be negative.")
        raise SystemExit

    print("\nWeights:", weights)
    print("Values:", values)
    print("Capacity:", capacity)

    knapsack(weights, values, capacity)
