def permutation(array, index=0,res=None):
    if res==None:
        res=[]

    if index==len(array):
        res.append(array[:])
        return
    for i in range(index, len(array)):
        array[index], array[i]=array[i], array[index]
        permutation(array,index+1, res)
        array[i], array[index]=array[index], array[i]
    return res
res=[]
print(permutation(array=[1,2,3],res=res))
print(res)

