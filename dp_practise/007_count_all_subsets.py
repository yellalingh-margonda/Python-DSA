def count_subset(arr, index,target_sum):
     if index==len(arr):
         return 0
     if target_sum==0:
         return 1
     count=0
     if target_sum-arr[index] >= 0:
        count+=count_subset(arr, index+1,target_sum-arr[index])
     count += count_subset(arr, index + 1, target_sum)
     return count

