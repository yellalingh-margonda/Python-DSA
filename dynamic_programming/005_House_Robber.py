def house_robber(n,array):
    if n==0:
        return array[n]
    if n<0:
        return 0
    left =array[n]+house_robber(n-2, array)
    right=house_robber(n-1,array)
    return max(left,right)
print(house_robber(2,[1,3,1]))

def house_robber_memo(n, array, dp=None):
    if dp is None:
        dp=[-1]*len(array)
    if n==0:
        return  array[n]
    if n<0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    left =array[n]+house_robber_memo(n-2, array, dp)
    right=house_robber_memo(n-1, array,dp)
    dp[n]=max(right, left)
    return dp[n]
array=[104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
print(house_robber_memo(len(array)-1,array))


def house_robber_tabu(n, array, dp=None):
    if dp is None:
        dp=[-1]*(n+1)
    dp[0]=array[0]
    for i in range(1,n+1):
        left= array[i]+ (dp[i-2] if i>1  else 0)
        right=dp[i-1]
        dp[i]=max(left, right)
    return dp[n]
array=[104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
print(house_robber_tabu(len(array)-1,array))
