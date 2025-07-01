#https://leetcode.com/problems/climbing-stairs/description/

def ways(n):
    if n<=1:
        return 1
    return ways(n-1)+ways(n-2)
print(ways(3))

