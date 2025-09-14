from collections import deque
def topo_sort(adj):
    indgr = {node: 0 for node in adj}
    for u in adj:
        for v in adj[u]:
            indgr[v] += 1
    queue = deque([u for u in adj if indgr[u] == 0])
    topo=[]
    while queue:
        node = queue.popleft()
        topo.append(node)
        for nei in adj[node]:
            indgr[nei]-=1
            if indgr[nei]==0:
                queue.append(nei)
    if len(topo) != len(adj):
        return None  # cycle detected
    return topo

# Example
adj = {
    0: [],
    1: [2],
    2: [3],
    3: [],
    4: [0],
    5: [0, 2]
}
print(topo_sort(adj))  # [1, 4, 5, 2, 3, 0] (valid order)