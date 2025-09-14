
def bipartite(adj, node):
    color=[-1]*node
    queue=[0]
    color[0]=1
    while queue:
        node= queue.pop(0)
        for nei in adj[node]:
            if color[nei]==-1:
                color[nei]=1-color[node]
                queue.append(nei)
            elif color[nei]==color[node]:
                return False
    return True
adj = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]
adj = [
    [1, 2],  # Node 0 connected to 1 and 2
    [0, 2],  # Node 1 connected to 0 and 2
    [0, 1]   # Node 2 connected to 0 and 1
]

print(bipartite(adj, 4))  # Output: True (This graph is bipartite)
