lb=[0]
def lower_bond(array, target):
    lb=len(array)
    low=0
    high=len(array)-1
    while high>=low:
        mid=low+(high-low)//2
        if array[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return  lb
print(lower_bond([1,2,3,5,6,7,8], 3))


def upper_bond(array, target):
    ub=len(array)
    low=0
    high=len(array)-1
    while high>=low:
        mid=low+(high-low)//2
        if array[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return  ub
print(upper_bond([1,2,3,5,6,7,8], 3))
