def subarra_count(arr,k):
    count,n=0,len(arr)
    for i in range(n):
        hash_map=set()
        for j in range(i, n):
            hash_map.add(arr[j])
            if len(hash_map)==k:
                count+=1
            if len(hash_map)>k:
                break
    return count

def subarra_count_optimal(arr,k):
    if k<0:
        return 0
    l,count,n=0,0,len(arr)
    hash_map={}
    for r in range(n):
        hash_map[arr[r]]=hash_map.get(arr[r],0)+1
        while len(hash_map)>k:
            hash_map[arr[l]]-=1
            if hash_map[arr[l]]==0:
                del hash_map[arr[l]]
            l+=1
        count+=r-l+1
    return count
nums = [1,2,1,2,3]
k = 2
subarra_count_optimal(nums,k)-subarra_count_optimal(nums,k-1)