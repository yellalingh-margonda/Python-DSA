def power_set(array, path=None, index=0):
    if path==None:
        path=[]
    if index>=len(array):
        return [path[:]]
    path.append(array[index])
    left=power_set(array,path, index+1)
    path.pop()
    right=power_set(array,path, index+1)
    return left+right
print(power_set([1,2,3]))