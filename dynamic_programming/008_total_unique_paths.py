def total_uniqpath(i,j):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    up_count=total_uniqpath(i-1,j)
    left_count=total_uniqpath(i,j-1)
    return up_count+left_count

def total_uinque_paths_memo(i, j, dp =None):
    if dp is None:
        dp=[[-1 for _ in range(j+1)] for _ in range(i+1)]
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    up_count=total_uinque_paths_memo(i-1,j,dp)
    left_count=total_uinque_paths_memo(i,j-1,dp)
    dp[i][j]=up_count+left_count
    return dp[i][j]


def total_uinque_paths_tabulation(i, j, dp =None):
    if dp is None:
        dp=[[-1 for _ in range(j+1)] for _ in range(i+1)]
    for r in range(i + 1):
        dp[r][0] = 1
    for c in range(j + 1):
        dp[0][c] = 1
    for r in range(1, i+1):
        for c in range(1, j+1):
            up_count=dp[r-1][c] if r > 0 else 0
            left_count=dp[r][c-1] if c > 0 else 0
            dp[r][c]=up_count+left_count
    return dp[i][j]
print(total_uinque_paths_tabulation(i = 2,j  = 6))