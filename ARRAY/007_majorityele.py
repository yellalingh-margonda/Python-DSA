def majority(arr):
    n=len(arr)
    count=0
    candidate=None
    for ele in arr:
        if count==0:
            candidate=ele
            count+=1
        elif ele == candidate:
            count += 1
        else:
            count -= 1
    count=0
    for ele in arr:
        if ele ==candidate:
            count+=1
        if count>n/2:
            return candidate
    return -1