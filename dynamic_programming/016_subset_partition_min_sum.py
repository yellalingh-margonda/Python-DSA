def subset_sum_tabulation(array,target, dp=None):
    n=len(array)
    if dp is None:
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0]=True
    if array[0] <= target:
        dp[0][array[0]] = True

    for i in range(1,n):
        for t in range(1,target+1):
            take=False
            if t>=array[i]:
                take=dp[i-1][t-array[i]]
            not_take=dp[i-1][t]
            dp[i][t]=take or not_take
    return dp


arr = [8,6,5]
total_sum=sum(arr)
min_diff=float('inf')
n=len(arr)
dp=subset_sum_tabulation(arr,total_sum)
for s1 in range(total_sum + 1):
    if dp[n - 1][s1]:
        s2 = total_sum - s1
        diff = abs(s2 - s1)
        min_diff = min(min_diff, diff)

print(min_diff)  # Output: 1