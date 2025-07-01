def frog_jump(n,k, heights):
    if n==0:
        return 0
    level_res=float('inf')
    for j in range(1,k+1):
        if n - j >= 0:
            res=abs(heights[n]-heights[n-j])+frog_jump(n-j,k,heights)
            level_res=min(level_res, res)
    return level_res
heights = [10, 30, 40, 50, 20]
k = 3
n = len(heights)
print(frog_jump(n - 1, k, heights))  # Output: 30


def frog_jump_memo(n,k, heights, dp=None):
    if dp is None:
        dp=[-1]*(n+1)
        print(dp)
    if n==0:
        return 0

    if dp[n]!=-1:
        return dp[n]
    level_res=float('inf')
    for j in range(1,k+1):
        if n - j >= 0:
            res=abs(heights[n]-heights[n-j])+frog_jump_memo(n-j,k,heights,dp)
            level_res=min(level_res, res)
    dp[n]=level_res
    return dp[n]
heights = [10, 30, 40, 50, 20]
k = 3
n = len(heights)
print(frog_jump_memo(n-1, k, heights))  # Output: 30


def frog_jump_tab(n,k, heights, dp=None):
    if dp is None:
        dp=[-1]*(n+1)
        print(dp)
    dp[0]=0

    for i in range(1,n+1):
        level_res = float('inf')
        for j in range(1, min(i,k) + 1):
            if n - j >= 0:
                res=abs(heights[i]-heights[i-j])+dp[i-j]
                level_res=min(level_res, res)
        dp[i]=level_res

    return dp[n]
heights = [10, 30, 40, 50, 20]
k = 3
n = len(heights)
print(frog_jump_tab(n-1, k, heights))  # Output: 30
