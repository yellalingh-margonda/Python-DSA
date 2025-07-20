def longest_subarray(arr,k):
    l,r,maxi,current_sum=0,0,0,0
    n=len(arr)
    while r < n:
        current_sum += arr[r]
        while current_sum > k:
            current_sum -= arr[l]
            l+=1
        if current_sum <= k:
            maxi=max(maxi, r-l+1)
        r+=1
    return maxi

