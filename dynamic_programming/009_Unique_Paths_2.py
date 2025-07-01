def total_uniqpath(i,j, grid):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    up_count=total_uniqpath(i-1,j,grid) if grid[i-1][j]!=-1 else 0
    left_count=total_uniqpath(i,j-1,grid) if grid[i][j-1]!=-1 else 0
    return up_count+left_count

def total_uniqpath_memo(i,j, grid,dp=None):
    if dp is None:
        dp=[[-1 for _ in range(j)] for _ in range(i)]
    if i==0 and j==0:
        return 1
    if dp[i][j]!=-1:
        return dp[i][j]
    up_count=total_uniqpath_memo(i-1,j,grid,dp) if i >= 1 and grid[i-1][j]!=-1 else 0
    left_count=total_uniqpath_memo(i,j-1,grid,dp) if j >= 1 and grid[i][j-1]!=-1 else 0
    return up_count+left_count

def total_uniqpath_tabulation(i,j, grid,dp=None):
    if dp is None:
        dp=[[-1 for _ in range(j)] for _ in range(i)]
    for r in range(i + 1):
        dp[r][0] = 1
    for c in range(j + 1):
        dp[0][c] = 1
    for r in range(1,i+1):
        for c in range(1,j+1):
            up_count=dp[i-1][j] if i >= 1 and grid[i-1][j]!=-1 else 0
            left_count=dp[i][j-1] if j >= 1 and grid[i][j-1]!=-1 else 0
    return up_count+left_count
