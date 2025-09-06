def possible(array, d, limit):
    days=1
    capacity=0
    for w in array:
        if capacity+w<=limit:
            capacity+=w
        else:
            days+=1
            capacity=w
    return days<=d
def min_capacity(array, d):
    low = max(array)          # can't go lower than the heaviest item
    high = sum(array)         # worst case: carry everything in 1 day
    result = high

    while low <= high:
        mid = (low + high) // 2
        if possible(array, d, mid):
            result = mid       # possible — try smaller
            high = mid - 1
        else:
            low = mid + 1      # not possible — need bigger capacity

    return result