
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
    def display(self):
        for node in self.graph:
            print(f"{node} is connected to {self.graph[node]}")
g = Graph() 
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.display()
