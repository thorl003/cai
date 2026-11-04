
# Maximum Flow using Ford-Fulkerson Algorithm
# Runtime Input

from collections import deque

def bfs(graph, source, sink, parent):
    n = len(graph)

    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == sink:
                    return True

    return False


def max_flow(graph, source, sink):
    n = len(graph)
    parent = [-1] * n
    flow = 0

    while bfs(graph, source, sink, parent):

        path_flow = float('inf')
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        flow += path_flow

    return flow


# Runtime Input
n = int(input("Enter number of vertices: "))

graph = []

print("Enter capacity matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex (0 to n-1): "))
sink = int(input("Enter sink vertex (0 to n-1): "))

if source < 0 or source >= n or sink < 0 or sink >= n:
    print("Invalid source or sink vertex")
elif source == sink:
    print("Source and sink must be different")
else:
    result = max_flow(graph, source, sink)
    print("Maximum Flow:", result)
