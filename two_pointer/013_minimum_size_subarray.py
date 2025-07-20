def minimum_size(arr,target):
    l, n = 0, len(arr)
    current_sum=0
    mini =float('inf')
    for r in range(n):
        current_sum += arr[r]
        while current_sum>=target:
            mini=min(mini,r-l+1)
            current_sum-=arr[l]
            l+=1
    return mini if mini<float('inf') else 0