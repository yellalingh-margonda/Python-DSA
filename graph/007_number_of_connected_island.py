def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        # Base cases for recursion
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or visited[r][c]:
            return

        visited[r][c] = True

        # Explore neighbors
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Iterate through the grid to find new islands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                islands += 1
                dfs(r, c)  # Sink the entire island

    return islands