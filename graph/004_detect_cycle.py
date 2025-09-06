def cycle_detect(adj, nodes):
    queue=[(1,-1)]
    visited=[False]*nodes
    while queue:
        node, prev_node=queue.pop(0)
        visited[node]=True
        for nei in adj[node]:
            if not visited[nei]:
                queue.append((nei, node))
            elif nei != prev_node:
                return True  # cycle detected
    return  False
adj = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
nodes = 4

print(cycle_detect(adj,nodes))