def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    shapes = set()

    def dfs(r, c, base_r, base_c, shape):
        # Base case
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == '0' or visited[r][c]:
            return

        visited[r][c] = True
        shape.append((r - base_r, c - base_c))

        # Explore neighbors
        dfs(r + 1, c, base_r, base_c, shape)
        dfs(r - 1, c, base_r, base_c, shape)
        dfs(r, c + 1, base_r, base_c, shape)
        dfs(r, c - 1, base_r, base_c, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                shape = []
                dfs(r, c, r, c, shape)
                shapes.add(tuple(sorted(shape)))

    return len(shapes)
