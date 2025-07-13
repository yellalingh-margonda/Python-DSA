def subseq_sum(array, i , target):
    if target==0:
        return True
    if i < 0:
        return False
    take=False
    if array[i] <= target:
        take=subseq_sum(array, i-1, target-array[i])
    not_take=subseq_sum(array, i-1, target)

    return take or not_take

def subseq_sum_memo(array, i , target,dp=None):
    if dp is None:
        dp=[[-1 for _ in range(target+1)] for _ in range(len(array))]
    if target==0:
        return True
    if i < 0:
        return False
    if dp[i][target]!=-1:
        return dp[i][target]
    take=False
    if array[i] <= target:
        take=subseq_sum_memo(array, i-1, target-array[i],dp)
    not_take=subseq_sum_memo(array, i-1, target,dp)
    dp[i][target]=take or not_take
    return dp[i][target]
array=[2,3,1,1]
target=4
print(subseq_sum_memo(array,len(array)-1,target))

def subseq_sum_tabulation(array, target,dp=None):
    n=len(array)
    if dp is None:
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
    for i in range(len(array)):
        dp[i][0]=True #zero sum case
    if array[0] <= target:#sum equal to every element in array can be formed
        dp[0][array[0]] = True
    for i in range(n):
        for t in range(1,target+1):
            take=dp[i-1][t-array[i]] if t>=array[i] else False
            not_take=dp[i-1][t]
            dp[i][t]=take or not_take
    return dp[n-1][target]
array=[2,3,1,1]
target=5
print("asdsadsadsa")
print(subseq_sum_tabulation(array,target))
