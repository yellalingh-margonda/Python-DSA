def subarray_sum(arr,k):
    prefix_sum = [arr[0]]
    n = len(arr)

    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    prefix_map = {0: 1}
    count = 0
    for i in range(n):
        if prefix_sum[i] - k in prefix_map:
            count += prefix_map[prefix_sum[i] - k]
        prefix_map[prefix_sum[i]] = prefix_map.get(prefix_sum[i], 0) + 1
    return count
arr = [1, 2, 3]
k = 3
print(subarray_sum(arr, k))  # Output: 2 ([1,2] and [3])
