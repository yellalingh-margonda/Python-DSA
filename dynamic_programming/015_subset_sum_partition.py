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

def subset_sum_parition(array):
    if sum(array)%2!=0:
        return False
    target=sum(array)/2
    return subseq_sum(array,len(array)-1,target)
array=[2,3,3,3,4,5,2,4]
print(subset_sum_parition(array))

def subseq_sum_memo(array, i , target,dp=None):
    n=len(array)
    if dp is None:
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
    if target==0:
        return True
    if i < 0:
        return False
    take=False
    if dp[i][target]!=-1:
        return dp[i][target]

    if array[i] <= target:
        take=subseq_sum_memo(array, i-1, target-array[i],dp)
    not_take=subseq_sum_memo(array, i-1, target,dp)
    dp[i][target]=take or not_take
    return dp[i][target]

def subset_sum_parition_memo(array):
    if sum(array) % 2 != 0:
        return False
    target = sum(array) / 2
    return subseq_sum_memo(array, len(array) - 1, int(target))
array=[2,3,3,3,4,5,2,4]
print(subset_sum_parition_memo(array))