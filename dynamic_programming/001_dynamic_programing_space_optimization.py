#tabulation Bottom up
#memo top down
#fib num

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(5))

#top down approach we caliculate the 
def fib_memo(n, dp=None):
    if dp is None:
        dp=[-1 for _ in range(n+1)] #step 0 declare the dp
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n] #step 2 check if dp[n] is not equal to default value
    dp[n]=fib_memo(n-1, dp)+fib_memo(n-2, dp) # step 3caliculate the dp value
    return dp[n]
print(fib_memo(5))

#bottom up start from base case and go to solution
def fib_tabulation(n, dp=None):
    if dp is None:
        dp=[-1 for _ in range(n+1)]
    #base cases
    dp[0], dp[1]=0,1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(fib_tabulation(5))

def fib_tabulation_optimization(n):
    prev=1
    prev2=0
    for _ in range(2,n+1):
        current=prev+prev2 # as wecan see the current state depens only previous twostates, so we use only two varibale to hold previous two states
        prev2=prev
        prev=current
    return  current
print(fib_tabulation_optimization(5))



