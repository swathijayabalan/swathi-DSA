
class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.edges = [] 
    
    def add_edge(self, u, v):
        self.edges.append((u, v)) 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])  
    def union(self, parent, x, y):
        parent[x] = y
    def kruskal_mst(self):
        mst = []  
        parent = list(range(self.V))  
        self.edges.sort()
        for u, v in self.edges:
            parent_u = self.find(parent, u)
            parent_v = self.find(parent, v)
            if parent_u != parent_v:
                mst.append((u, v)) 
                self.union(parent, parent_u, parent_v)  
        print("The edges in the Minimum Spanning Tree (MST) are:")
        for u, v in mst:
            print(f"{u} -- {v}")
g = Graph(4) 
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.kruskal_mst()
