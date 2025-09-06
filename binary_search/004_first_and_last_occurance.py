def first_last_occurance(arr, target):
    low, high=0,len(arr)-1
    while low<=high:
        mid =low+(high-low)//2
        if arr[mid]==target:
            i = mid
            while i >-1 and arr[i-1]==arr[mid]:
                i=i-1

            j = mid
            while j < len(arr) and arr[j+1] == arr[mid]:
                j = j + 1
            return [i, j]
        if arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return [-1,-1]
nums = [5,7,7,8,8,10]
target = 8
print(first_last_occurance(nums,target))
#approach 2

def firstAndLastPosition(arr, n, k):
    def lower_bound(arr, k, n):
        start, end = 0, n - 1
        ans = n
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] >= k:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def upper_bound(arr, k, n):
        start, end = 0, n - 1
        ans = n
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] > k:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    lb = lower_bound(arr, k, n)
    ub = upper_bound(arr, k, n)

    if lb == n or arr[lb] != k:
        return [-1, -1]
    return [lb, ub - 1]
