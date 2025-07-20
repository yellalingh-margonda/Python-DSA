def subsets(arr,path,index):
    if index>len(arr):
        return 0
    if index==len(arr):
        return 1
    count=-0
    path.append(arr[index])
    count+=subsets(arr,path,index+1)
    path.pop()
    count+=subsets(arr,path,index+1)
    return count

print(subsets([1,2,3],[],0))