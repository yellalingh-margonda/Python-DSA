def subset_sum(array, index=0,path=None):
    if path==None:
        path=[]
    if index == 0:
        array.sort()
    subsets = [path[:]]
    for i in range(index,len(array)):
        if i>index and array[i]==array[i-1]:
            continue
        path.append(array[i])
        subsets+=subset_sum(array, i+1,path)
        path.pop()
    return subsets
print(subset_sum([1,2,2]))