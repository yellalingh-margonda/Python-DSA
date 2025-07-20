#represents number of ways to climb n striars
def climb_strain_count(n):
    if n<=2:
        return n
    return climb_strain_count(n-1)+climb_strain_count(n-2)

def climb_strain_memo(n,dp=None):
    if dp is None:
        dp=[-1]*(n+1)
    if n<=2:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=climb_strain_count(n-1,dp)+climb_strain_count(n-2,dp)
    return dp[n]

def climb_strain_tabu(n,dp=None):
    if dp is None:
        dp=[-1]*(n+1)
    dp[0],dp[1]=0,1
    if n>=2:
        dp[2]=2

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]