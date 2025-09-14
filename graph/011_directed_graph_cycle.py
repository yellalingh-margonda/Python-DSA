def dfs(adj, visited, recStack, node):
    # Mark current node as visited and part of recursion stack
    visited[node] = True
    recStack[node] = True

    for nei in adj[node]:
        # If neighbor not visited, recurse on it
        if not visited[nei]:
            if dfs(adj, visited, recStack, nei):
                return True
        # If neighbor in recursion stack -> cycle detected
        elif recStack[nei]:
            return True

    # Remove node from recursion stack before returning
    recStack[node] = False
    return False

def cycle_detection(adj):
    n = len(adj)
    visited = [False] * n
    recStack = [False] * n

    for node in range(n):
        if not visited[node]:
            if dfs(adj, visited, recStack, node):
                return True
    return False
