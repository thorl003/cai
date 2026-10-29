def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # Reconstruct LCS
    i, j = m, n
    sequence = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            sequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    sequence.reverse()
    result = "".join(sequence)

    # Display results
    print("\nDP Table:")
    for row in dp:
        print(*row)

    print("\nLongest Common Subsequence:", result)
    print("LCS Length:", dp[m][n])

if __name__ == "__main__":
    X = input("Enter first string: ")
    Y = input("Enter second string: ")

    lcs(X, Y)
