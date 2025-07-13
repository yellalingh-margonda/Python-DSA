def max_sum(i,j, grid):
    if i < 0 or j < 0 or j >= len(grid[0]):
        return float('-inf')
    if i==0:
        return grid[i][j]
    up=max_sum(i-1,j,grid)
    left=max_sum(i-1,j-1,grid)
    right=max_sum(i-1,j+1,grid)
    return grid[i][j]+max(up,left,right)

grid = [
    [10, 10, 2, 0, 20, 4],
    [1, 0, 0, 30, 2, 5],
    [0, 10, 4, 0, 2, 0],
    [1, 0, 2, 20, 0, 4]
]

m, n = len(grid), len(grid[0])
col_max=float('-inf')
for j in range(n):
    col_max=max(col_max, max_sum(m-1,j,grid))
print(col_max)


def max_sum_memo(i,j, grid,dp):
    if i < 0 or j < 0 or j >= len(grid[0]):
        return float('-inf')
    if i==0:
        return grid[i][j]
    if dp[i][j]!=-1:
        return dp[i][j]
    up=max_sum_memo(i-1,j,grid,dp)
    left=max_sum_memo(i-1,j-1,grid,dp)
    right=max_sum_memo(i-1,j+1,grid,dp)
    dp[i][j]=grid[i][j]+max(up,left,right)
    return dp[i][j]

grid = [
    [10, 10, 2, 0, 20, 4],
    [1, 0, 0, 30, 2, 5],
    [0, 10, 4, 0, 2, 0],
    [1, 0, 2, 20, 0, 4]
]

m, n = len(grid), len(grid[0])
col_max=float('-inf')
for j in range(n):
    dp=[[-1 for _ in range(n)]for _ in range(m)]
    col_max=max(col_max, max_sum_memo(m-1,j,grid,dp))
print(col_max)


def max_sum_tabulation(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Base case: first row is the same as grid
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill the dp table from row 1 to m-1
    for i in range(1, m):
        for j in range(n):
            up = dp[i - 1][j]
            left = dp[i - 1][j - 1] if j - 1 >= 0 else float('-inf')
            right = dp[i - 1][j + 1] if j + 1 < n else float('-inf')
            dp[i][j] = grid[i][j] + max(up, left, right)
    # Maximum in the last row
    return max(dp[m - 1])


grid = [
    [10, 10, 2, 0, 20, 4],
    [1, 0, 0, 30, 2, 5],
    [0, 10, 4, 0, 2, 0],
    [1, 0, 2, 20, 0, 4]
]

m, n = len(grid), len(grid[0])
grid = [
    [10, 10, 2, 0, 20, 4],
    [1, 0, 0, 30, 2, 5],
    [0, 10, 4, 0, 2, 0],
    [1, 0, 2, 20, 0, 4]
]

print(max_sum_tabulation(grid))  # ✅ Output: 74
