def frog_jum(i, nums):
    if i==0:
         return 0

    left= abs(nums[i]-nums[i-1])+frog_jum(i-1, nums)
    right= float('inf')
    if i-1>0:
        right= abs(nums[i]-nums[i-2])+frog_jum(i-2, nums)

    return min(left,right)

nums = [10, 30, 40, 20]
n = len(nums)
print(frog_jum(n - 1, nums))  # Output should be 30

def frog_jump_memo(i, heights, dp=None):
    if dp is None:
        dp = [-1] * len(heights)

    if i == 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    # Cost from previous stone
    left = frog_jump_memo(i - 1, heights, dp) + abs(heights[i] - heights[i - 1])

    # Cost from skipping one stone
    right = float('inf')
    if i > 1:
        right = frog_jump_memo(i - 2, heights, dp) + abs(heights[i] - heights[i - 2])

    dp[i] = min(left, right)
    return dp[i]

# Example
heights = [10, 30, 20, 40]
n = len(heights)
print(frog_jump_memo(n - 1, heights))  # Output: 30


def frog_jump_tabulation(heights, dp=None):
    if dp is None:
        dp = [-1] * len(heights)
    dp[0]=0

    for i in  range(1,n):
        left= dp[i - 1] + abs(heights[i] - heights[i - 1])
        right=float('inf')
        if i>1:
            right =dp[i - 2] + abs(heights[i] - heights[i - 2])
        dp[i]=min(left,right)
    return dp[len(heights)-1]
print(frog_jump_tabulation(heights))

def frog_jump_space(heights):
    prev2=0
    prev = min(prev2,abs(heights[0]-heights[1]))

    for i in range(1, n):
        left = prev + abs(heights[i] - heights[i - 1])
        right = float('inf')
        if i > 1:
            right = prev2 + abs(heights[i] - heights[i - 2])
        current = min(left, right)
        prev2=prev
        prev=current
    return current
heights = [10, 30, 20, 40]
print(frog_jump_space(heights))
