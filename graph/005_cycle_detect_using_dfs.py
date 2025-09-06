def dfs(adj,n, node,prev, visited=None):
    if visited is None:
        visited=[0]*n
    visited[node]=1
    for nei in adj[node]:
        if visited[nei]==0:
            if dfs(adj, n, nei, node, visited):
                return True
        elif nei != prev:
            return True
    return False



