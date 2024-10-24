import sys
def find_min_key_node(keys, mst_set, V):
    min_value = sys.maxsize
    
    min_index = -1
    for v in range(V):
        if keys[v] < min_value and not mst_set[v]:
            min_value = keys[v]
            min_index = v
    return min_index
def print_mst(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def prim_mst(graph, V):
    keys = [sys.maxsize] * V  
    parent = [None] * V 
    mst_set = [False] * V  
    keys[0] = 0
    parent[0] = -1  
    for _ in range(V):
        u = find_min_key_node(keys, mst_set, V)
        mst_set[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not mst_set[v] and keys[v] > graph[u][v]:
                keys[v] = graph[u][v]
                parent[v] = u
    print_mst(parent, graph, V)

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

V = len(graph)
prim_mst(graph, V)
