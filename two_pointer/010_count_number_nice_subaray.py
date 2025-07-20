
def nice_subarray(array, k):
    if k<0:
        return 0
    l,count, n, current_sum = 0, 0,len(array), 0
    for r in range(n):
        current_sum+=array[r]%2
        while current_sum>k:
            current_sum-=array[l]%2
            l+=1
        count+=r-l+1
    return count
nums = [1,1,2,1,1]
k = 3
print(nice_subarray(nums,k)-nice_subarray(nums,k-1))