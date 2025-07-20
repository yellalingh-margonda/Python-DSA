def subsets(arr,path,index):
    if index==len(arr):
        return [path[:]]
    path.append(arr[index])
    take=subsets(arr,path,index+1)
    path.pop()
    not_take=subsets(arr,path,index+1)
    return take+not_take

print(subsets([1,2,3],[],0))