def max_points(arr,k):
    left_sum, right_sum, maxi, right_index=0,0,0,len(arr)-1
    for i in range(k):
        left_sum+=arr[i]
    maxi=max(maxi,left_sum)

    for i in range(k-1, -1, -1):
        left_sum-=arr[i]
        right_sum+=arr[right_index]
        maxi=max(maxi,left_sum+right_sum)
        right_index-=1
    return maxi

