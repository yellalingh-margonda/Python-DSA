def search_binary(arry,target):
    low=0
    high=len(arry)-1

    while low<=high:
        mid = (low + high) // 2
        if arry[mid]==target:
            return  mid
        if arry[mid]< target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(search_binary([1,2,3,4,5,6,7,8],13))
