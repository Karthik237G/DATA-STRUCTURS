#adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.display()

#adjacency matrix
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Usage
g = Graph(4)  # 4 vertices
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.display()

