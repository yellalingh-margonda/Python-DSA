def rainwater(array):
    n=len(array)
    total=0
    left_max=[0]*n
    right_max=[0]*n
    left_max[0]=array[0]
    right_max[n-1]=array[n-1]
    for i in range(1,n):
        left_max[i]=max(left_max[i-1],array[i])
    for i in range(n-2, -1, -1):
        right_max[i]=max(right_max[i+1], array[i])
    for i in range(n):
        total+=min(left_max[i],right_max[i])-array[i]
    return total