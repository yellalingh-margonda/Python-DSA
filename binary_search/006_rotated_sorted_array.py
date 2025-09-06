def search(arr, n, k):
    start, end = 0, n-1

    while start <= end:
        mid = start+(end-start)//2
        if arr[mid] == k:
            return mid
        if arr[start] == arr[end] and arr[end] == arr[mid]:
            start += 1
            end -= 1
            continue
        if arr[start] <= arr[mid]:
            if arr[start] <= k < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if arr[mid] < k <= arr[end]:
                start = mid+1
            else:
                end = mid-1
    return -1
