
# Graph Coloring using Backtracking
# Runtime Input

def is_safe(graph, color, vertex, c, n):
    for i in range(n):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring(graph, m, color, vertex, n):

    if vertex == n:
        return True

    for c in range(1, m + 1):

        if is_safe(graph, color, vertex, c, n):

            color[vertex] = c

            if graph_coloring(graph, m, color, vertex + 1, n):
                return True

            color[vertex] = 0

    return False


# Runtime Input
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of colors: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

color = [0] * n

if graph_coloring(graph, m, color, 0, n):
    print("\nGraph Coloring is possible")
    for i in range(n):
        print("Vertex", i + 1, ":", "Color", color[i])
else:
    print("\nGraph Coloring is not possible")
