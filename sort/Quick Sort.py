# Approach: Picks a pivot, partitions the array so all smaller elements come before and larger ones after. After partitioning, the pivot is in its correct final position.
#
# Key Observation: After each partition step, the pivot is fixed in its correct place.
#
# Time: Avg O(n log n), Worst O(n²), Space: O(log n)

def qick_Sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return qick_Sort(left)+[pivot]+qick_Sort(right)
print(qick_Sort([1,5,2,-1,-11]))