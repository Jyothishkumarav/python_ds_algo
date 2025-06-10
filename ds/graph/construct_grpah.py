# # create a Graph class that takes edges like [(u1, v1), (u2, v2), ...] and builds an undirected graph.
# edges = [
#     (0, 1),
#     (0, 2),
#     (1, 3),
#     (2, 4),
#     (3, 4)
# ]
#
# g = Graph(edges)
# g.display()
from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.build_graph(edges)

    def build_graph(self, edges):
        for u,v in edges:
            self.graph[u].append(v)
    def display(self):
        for node in self.graph:
            print(f'{node} >>>  {self.graph[node]}')

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not  in visited:
                visited.add(node)
                result.append(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        results = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                results.append(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(node)
        return results


if __name__ == "__main__":
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (3, 4)
    ]

    g = Graph(edges)
    g.display()
    results = g.dfs(0)
    print(results)
