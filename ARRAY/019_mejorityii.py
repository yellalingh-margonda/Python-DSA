def mejority_ii(nums):
    res=[]
    n=len(nums)
    for i in range(n):
        if nums[i] != res[-1] or len(res) == 0:
            count=0
            for j in range(i, n):
                if nums[i] == nums[j]:
                    count += 1
            if count > n//2:
                res.append(nums[i])
            if len(res) == 2:
                return res

    return res

def majority_hash(nums):
    res_hash = {}
    n = len(nums)
    res=set()
    for i in range(n):
        count = res_hash.get(nums[i], 0)+1
        res_hash[nums[i]] = count
        if count > n//3:
            res.add(nums[i])
        if len(res) == 2:
            return list(res)
    return list(res)
print(majority_hash([1,2]))


def majority_optimal(nums):
    count1=0
    count2=0
    n=len(nums)
    ele1=None
    ele2=None
    limit=n//3
    for i in range(n):
        if count1 ==0 and nums[i] != ele2:
            count1 += 1
            ele1 = nums[i]
        elif count2 == 0 and nums[i] != ele1:
            count2 += 1
            ele2 = nums[i]
        elif ele1 == nums[i]:
            count1 += 1
        elif ele2 == nums[i]:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    res=[]
    count1,count2 =0,0
    for num in nums:
        if num==ele1:
          count1+=1
        elif num==ele2:
            count2+=1
        if count1>limit:
            res.append(ele1)
        if count2>limit:
            res.append(ele2)
    return  res