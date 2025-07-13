def dfs(i, total, arr, dp):
    if total == 0:
        return 1
    if i >= len(arr) or total < 0:
        return 0
    if dp[i][total] != -1:
        return dp[i][total]
    dp[i][total] = dfs(i + 1, total - arr[i], arr, dp) + dfs(i + 1, total, arr, dp)
    return dp[i][total]


arr=[12, 14, 3, 18, 2]
k=13
n = len(arr)
dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
print(dfs(0, k, arr, dp))