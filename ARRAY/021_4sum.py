def sum4_brute(arr):
    res=set()
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l]==0:
                        res.add(tuple(sorted([arr[i],arr[j],arr[k],arr[l]])))

    return [list(ele) for ele in res]


def sum4_better(arr):
    res=set()
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            hash_set = set()
            for k in range(j+1,n):
                fourth=-(arr[i]+arr[j]+arr[k])
                if fourth in hash_set:
                    res.add(tuple(sorted([arr[i],arr[j],arr[k],fourth])))
                hash_set.add(arr[k])
    return [list(ele) for ele in res]

def sum4_optimal(arr):
    res=[]
    arr.sort()
    n=len(arr)
    for i in range(n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue  # Skip duplicates for j
            fourth=-(arr[i]+arr[j])
            left, right = j+1,n-1
            while left<right:
                current_sum=arr[left]+arr[right]
                if current_sum==fourth:
                    res.append([arr[i],arr[j],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif current_sum>fourth:
                    right-=1
                else:
                    left+=1
    return  res
