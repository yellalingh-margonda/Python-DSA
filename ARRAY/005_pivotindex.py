def pivot_index(nums):
    n=len(nums)
    for i in range(1,n):
        nums[i]=nums[i-1]+nums[i]
    for i in range(n):
        if i==0 and nums[n-1]-nums[i]==0:
               return i
        if nums[i-1]==nums[n-1]-nums[i]:
            return i
    return -1
print(pivot_index([2,1,-1]))