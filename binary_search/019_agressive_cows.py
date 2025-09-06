def possible(array, n, d):
    count = 1
    last_position = array[0]
    for i in range(1, len(array)):
        if array[i] - last_position >= d:
            count += 1
            last_position = array[i]
        if count >= n:
            return True
    return False

def agressive_cows(array, n):
    array.sort()
    low=1
    high=max(array)
    ans=1
    while low<=high:
        mid=low+(high-low)//2
        if possible(array,n,mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

stalls= [10, 1, 2, 7, 5]
k = 3
print(agressive_cows(stalls,k))