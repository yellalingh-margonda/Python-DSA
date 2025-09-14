def findCircleNum(isConnected):
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    provinces = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            provinces += 1

    return provinces
