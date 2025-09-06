grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
m, n = len(grid), len(grid[0])


def bfs(grid, visited=None, queue=None):
    m, n = len(grid), len(grid[0])

    if visited is None:
        visited = [[False for _ in range(n)] for _ in range(m)]
    if queue is None:
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
                else:
                    visited[i][j] = False

    time = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        size = len(queue)
        infected_this_round = False

        for _ in range(size):
            i, j = queue.pop(0)

            for dir in directions:
                di, dj = i + dir[0], j + dir[1]

                if 0 <= di < m and 0 <= dj < n and not visited[di][dj] and grid[di][dj] == 1:
                    grid[di][dj] = 2
                    visited[di][dj] = True
                    queue.append((di, dj))
                    infected_this_round = True

        if infected_this_round:
            time += 1

    # Check if any fresh orange left
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1

    return time


print(bfs(grid))
