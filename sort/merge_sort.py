def merge_array(left,right):
    i,j=0,0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i< len(left):
        res.extend(left[i:])
    if j< len(right):
        res.extend(right[j:])
    return res

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left=merge_sort(nums[:mid])
    right=merge_sort(nums[mid:])
    return merge_array(left,right)
print(merge_sort([7,2,1,6,3,9,5]))