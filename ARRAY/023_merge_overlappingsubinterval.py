
nums=[[1,3],[8,10],[15,18],[2,6]]



def merge_brut(nums):
    nums=sorted(nums)
    res=[]
    i,n=0,len(nums)
    while i<n:
        start=nums[i][0]
        end=nums[i][1]
        while i+1<n and nums[i][1]>nums[i+1][0]:
            end=nums[i+1][1]
            i+=1
        res.append([start,end])
        i+=1
    return res
print(merge_brut(nums))