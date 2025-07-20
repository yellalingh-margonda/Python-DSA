def subarraysum(arr,k):
    if k<0:
        return 0
    l,n, current_sum,count=0,len(arr),0,0
    for r in range(n):
        current_sum+=arr[r]
        while current_sum>k:
             current_sum-=arr[l]
             l+=1
        count+=r-l+1
    return count

nums = [1,0,1,0,1]
goal = 2
print(subarraysum(nums,goal)-subarraysum(nums,goal-1))