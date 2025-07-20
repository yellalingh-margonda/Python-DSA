def most_consicutive_ones(arr,k):
    l,n, maxi=0,len(arr),0
    k_count=0
    for r in range(n):
        if arr[r]==0:
            k_count+=1
        while k_count>k:
            if arr[l] == 0:
                k_count -= 1
            l += 1
        maxi=max(maxi, r-l+1)
    return  maxi

nums = [1,1,1,0,0,0,1,1,1,1,0]
k=2
print(most_consicutive_ones(nums,k))