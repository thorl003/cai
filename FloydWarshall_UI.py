INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = []

    print("Enter adjacency matrix (use INF for no direct edge):")

    for i in range(n):
        row = input().split()

        if len(row) != n:
            print(f"Error: Enter exactly {n} values per row.")
            raise SystemExit

        graph.append([
            INF if value.upper() == "INF" else float(value)
            for value in row
        ])

    shortest_paths = floyd_warshall(graph)

    print("Shortest Distance Matrix:")
    for row in shortest_paths:
        print([
            "INF" if val == INF else int(val) if val.is_integer()
            else val
            for val in row
        ])
