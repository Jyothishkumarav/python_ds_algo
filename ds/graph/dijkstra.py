import heapq

def dijkstra(graph, start):
    """
    graph: adjacency list where graph[u] = [(v, weight), ...]
    start: starting vertex
    returns: list of shortest distances from start to all vertices
    """
    n = len(graph)
    dist = [float('inf')] * n  # Distance to each vertex
    dist[start] = 0

    # Priority queue: (distance, vertex)
    min_heap = [(0, start)]

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        # Skip if we already found a better path
        if curr_dist > dist[u]:
            continue

        # Explore all neighbors
        for neighbor, weight in graph[u]:
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                heapq.heappush(min_heap, (dist[neighbor], neighbor))

    return dist
if __name__ == '__main__':
    # Create a weighted directed graph with 5 vertices (0 to 4)
    graph = [
        [(1, 2), (2, 4)],  # 0 -> 1 (2), 0 -> 2 (4)
        [(2, 1), (3, 7)],  # 1 -> 2 (1), 1 -> 3 (7)
        [(4, 3)],  # 2 -> 4 (3)
        [(4, 1)],  # 3 -> 4 (1)
        []  # 4 has no outgoing edges
    ]

    # Find shortest paths from node 0
    distances = dijkstra(graph, 0)
    print("Shortest distances from node 0:", distances)
