def minimum_path_sum(i,j, grid):
    if i==0 and j==0:
        return grid[i][j]
    if i<0 or j<0:
        return float('inf')
    up_count=grid[i][j]+minimum_path_sum(i-1,j,grid)
    left_count=grid[i][j]+minimum_path_sum(i,j-1,grid)
    return min(up_count,left_count)
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minimum_path_sum(2,2,grid))

def minimum_path_sum_memo(i,j, grid, dp=None):
    if dp is None:
        dp=[[float('inf') for _ in range(j+1)] for _ in range(i+1)]
    if i==0 and j==0:
        return grid[i][j]
    if i<0 or j<0:
        return float('inf')
    if dp[i][j]!=float('inf'):
        return dp[i][j]
    up_count=grid[i][j]+minimum_path_sum_memo(i-1,j,grid,dp)
    left_count=grid[i][j]+minimum_path_sum_memo(i,j-1,grid,dp)
    dp[i][j]=min(up_count,left_count)
    return dp[i][j]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minimum_path_sum_memo(2,2,grid))

def minimum_path_sum_tabulation(i,j, grid, dp=None):
    if dp is None:
        dp=[[float('inf') for _ in range(j+1)] for _ in range(i+1)]
    dp[0][0]=grid[0][0]
    for r in range(i+1):
        for c in range(j+1):
            if r==0 and c==0:
                continue
            up_count=grid[r][c]+dp[r-1][c] if r>0 else float('inf')
            left_count=grid[r][c]+dp[r][c-1] if c>0 else float('inf')
            dp[r][c]=min(up_count,left_count)
    return dp[i][j]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minimum_path_sum_memo(2,2,grid))

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minimum_path_sum_tabulation(2,2,grid))