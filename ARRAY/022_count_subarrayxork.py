def subarra_xor(arr,k):
    n=len(arr)
    prefix_xor=[arr[0]]
    for i in range(1, n):
        prefix_xor.append(prefix_xor[-1]^arr[i])
    prefix_map = {0: 1}
    count = 0
    for i in range(n):
        if prefix_xor[i]^k in prefix_map:
            count += prefix_map[prefix_xor[i]^k]
        prefix_map[prefix_xor[i]] = prefix_map.get(prefix_xor[i], 0) + 1
    return count


