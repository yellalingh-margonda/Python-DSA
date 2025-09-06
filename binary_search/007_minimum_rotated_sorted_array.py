def find_min(arr, n):
    start, end = 0, n - 1
    mini = float('inf')

    while start <= end:
        mid = start + (end - start) // 2

        # If duplicates
        if arr[start] == arr[mid] == arr[end]:
            mini = min(mini, arr[mid])
            start += 1
            end -= 1
            continue

        # If left half is sorted
        if arr[start] <= arr[mid]:
            mini = min(mini, arr[start])
            start = mid + 1
        # Right half is sorted
        else:
            mini = min(mini, arr[mid])
            end = mid - 1

    return mini if mini != float('inf') else None


# Example
nums = [2, 2, 2, 0, 1]
print(find_min(nums, len(nums)))  # 0
