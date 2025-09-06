def search(arr, n, k):
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid

        # Left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < k <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, len(nums), target))  # 4
