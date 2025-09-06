def find_min_index(arr, n):
    start, end = 0, n - 1
    min_val = float('inf')
    min_index = -1

    while start <= end:
        mid = start + (end - start) // 2

        # Handle duplicates
        if arr[start] == arr[mid] == arr[end]:
            if arr[mid] < min_val:
                min_val = arr[mid]
                min_index = mid
            start += 1
            end -= 1
            continue

        # Left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] < min_val:
                min_val = arr[start]
                min_index = start
            start = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < min_val:
                min_val = arr[mid]
                min_index = mid
            end = mid - 1

    return min_index


# Example
nums = [2, 2, 2, 0, 1]
print(find_min_index(nums, len(nums)))  # 3
