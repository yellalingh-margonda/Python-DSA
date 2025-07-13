#https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628
def subset_count_memo(i, array, target, dp=None):
    n = len(array)
    if dp is None:
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

    if i == 0:
        if target == 0 and array[0] == 0:
            return 2
        if target == 0 or target == array[0]:
            return 1
        return 0
    if dp[i][target] != -1:
        return dp[i][target]
    take = 0
    if array[i] <= target:
        take = subset_count_memo(i - 1, array, target - array[i], dp)
    not_take = subset_count_memo(i - 1, array, target, dp)
    dp[i][target] = take + not_take
    return dp[i][target]

arr=[5, 2, 5, 1]
D=3
#s1-s2=d
#total=s1+s2
#total-s2=s1
#total-s2-s2=d
#2s2=total-d
#s2=(total-d)/2
total=sum(arr)
s2=(total-D)/2

