def next_permutation(arr):
    idx = -1
    n = len(arr)
    for i in range(n-2, -1, -2):
        if arr[i] < arr[i+1]:
            idx = i
            break
    if idx==-1:
        return arr[::-1]

    for i in range(n-1,idx,-1):
        if arr[i]>arr[idx]:
            arr[i],arr[idx]=arr[idx],arr[i]
            break

    arr[idx+1:].sort()
    return arr

nums = [1,2,3]
print(next_permutation(nums))
