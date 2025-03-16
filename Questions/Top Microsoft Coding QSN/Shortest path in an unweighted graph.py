import heapq


def shortestPath(edges, n, m, s, t):
    # Create adjacency list representation
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(graph, start):
        distances = [float('inf')] * len(graph)
        distances[start] = 0
        visited = [False] * len(graph)
        pq = [(0, start)]
        parent = [-1] * len(graph)

        while pq:
            (dist, node) = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances, parent

    distances, parent = dijkstra(graph, s)

    if distances[t] == float('inf'):
        return [-1]

    # Reconstruct path
    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    return path[::-1]


if __name__ == "__main__":
    n=4
    m=4
    s=2
    t=1
    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 2]]
    output = [2, 1]
    result = shortestPath(edges, n, m, s, t)
    print(*result)