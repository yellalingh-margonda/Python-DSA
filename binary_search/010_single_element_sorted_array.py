nums= [1,1,2,2,3,3,4,5,5,6,6]
#index (array[even]=array[odd]) the element is in right half even=odd-1
##index (array[even]=array[odd]) the element is in right half odd=even-1
#(even, odd)
#(odd, even)
def find_single(array):
    start, end = 0, len(array)-1
    if len(array)==1:
        return array[0]
    if array[0]!=array[1]:
        return array[0]
    if array[end]!=array[end-1]:
        return array[end]
    while start <= end:
        mid = start+(end-start)//2
        if array[mid]!=array[mid-1]  and array[mid]!=array[mid+1]:
            return array[mid]
        if (mid%2==1 and array[mid]==array[mid-1]) or (mid%2==0 and array[mid]==array[mid+1]):
            start=mid+1
        else:
            end=mid-1
    return -1
print(find_single(nums))