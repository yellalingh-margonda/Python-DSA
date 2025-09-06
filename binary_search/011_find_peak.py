def find_peak(array):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2

        # Check if mid is a peak
        if (mid == 0 or array[mid] >= array[mid - 1]) and \
           (mid == len(array) - 1 or array[mid] >= array[mid + 1]):
            return array[mid]

        # If right neighbor is bigger, peak is on the right
        if mid < len(array) - 1 and array[mid] < array[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return -1
print(find_peak([1, 2, 3, 1]))       # 3
print(find_peak([1, 2, 1, 3, 5, 6])) # 6
print(find_peak([5, 4, 3]))          # 5
