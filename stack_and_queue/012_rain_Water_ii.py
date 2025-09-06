def rainwater(array):
    left_max=0
    right_max=0
    l, r=0, len(array)-1
    total=0
    while l<r:
        if array[l]<=array[r]:
            if array[l]<left_max:
                total+= left_max-array[l]
            else:
                left_max=array[l]
            l+=1
        else:
            if array[r]<right_max:
                total+= right_max-array[r]
            else:
                right_max=array[r]
            r-=1
    return total
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(rainwater(height))