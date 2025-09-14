def dfs(node, adj, visited, ans):
    visited[node] = True
    for nei in adj[node]:
        if not visited[nei]:     # skip already visited neighbors
            dfs(nei, adj, visited, ans)
    ans.append(node)             # postorder → topo order


def topological_sort(adj):
    n = len(adj)
    visited = [False] * n
    ans = []

    for node in range(n):
        if not visited[node]:
            dfs(node, adj, visited, ans)

    return ans[::-1]   # reverse postorder gives topo sort


# Example
adj = {
    0: [],
    1: [2],
    2: [3],
    3: [],
    4: [0],
    5: [0, 2]
}

print(topological_sort(adj))  # [5, 4, 1, 2, 3, 0]
