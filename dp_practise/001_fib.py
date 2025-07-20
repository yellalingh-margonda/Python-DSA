
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def fib(n,dp =None):
    if dp is None:
        dp=[-1]*(n+1)
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]