def traingle(i, j,grid):

    if i==len(grid)-1:
        return grid[i][j]
    if i>len(grid)-1 or j>i:
        return 0
    down=traingle(i+1,j, grid)
    diag=traingle(i+1,j+1, grid)
    level_min=min(down,diag)
    return grid[i][j]+level_min
grid = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(traingle(0,0,grid))

def traingle_memo(i, j,grid,dp=None):
    if dp is None:
        dp=[[float('inf') for _ in row] for row in grid]
    if i==len(grid)-1:
        return grid[i][j]
    if i>len(grid)-1 or j>i:
        return 0
    if dp[i][j]!=float('inf'):
        return dp[i][j]
    down=traingle_memo(i+1,j, grid,dp)
    diag=traingle_memo(i+1,j+1, grid,dp)
    dp[i][j]=grid[i][j]+min(down,diag)
    return dp[i][j]
grid = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(traingle_memo(0,0,grid))

def traingle_tabulation(grid,dp=None):

    if dp is None:
        dp=[[float('inf') for _ in row] for row in grid]
    n = len(grid)
    for j in range(len(grid[n-1])):
        dp[len(grid)-1][j]=grid[len(grid)-1][j]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            down = dp[i + 1][j]
            diag = dp[i + 1][j + 1]
            dp[i][j]=grid[i][j]+min(down, diag)
    return dp[0][0]

grid = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(traingle_tabulation(grid))  # Output: 11
