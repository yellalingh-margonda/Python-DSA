def Sum3_brut(nums):
    res=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k]==0 and nums[i]!= nums[j] and nums[j]!= nums[k]:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
    return [list(ele) for ele in res ]

print(Sum3_brut( nums = [-1,0,1,2,-1,-4]))

# This code implements an optimized O(n²) solution to the 3Sum problem using hashing. For each element nums[i],
# it uses a hash_set to track the needed third value (-nums[i] - nums[j]) that would make the sum of a triplet zero.
# If the required third value is already in the set, a valid triplet is found. Each triplet is sorted and added as a
# tuple to a result set to avoid duplicates. Finally, the result is converted back to a list of lists for output.
# This avoids the brute-force O(n³) approach by reducing one loop through hashing.

def Sum3_better(nums):
    res=set()
    n=len(nums)
    for i in range(n):
        hash_set = set()
        for j in range(i+1,n):
            third=-(nums[i]+nums[j])
            if third in hash_set:
                triplet = tuple(sorted([nums[i], nums[j], third]))
                res.add(triplet)
            hash_set.add(nums[j])
    return [list(ele) for ele in res ]

print(Sum3_better( nums = [-1,0,1,2,-1,-4]))


# This function implements the optimal two-pointer approach to solve the 3Sum problem in O(n²) time.
# It first sorts the array and iterates through each element `nums[i]`, fixing it as the first element of a
# potential triplet. For each fixed element, it uses two pointers (`left` and `right`) to search for two other
# elements such that their sum with `nums[i]` is zero. When a valid triplet is found, it’s added to the result list,
# and the pointers are moved while skipping duplicates to avoid repeated triplets. However, there's a **bug**: the return statement is incorrectly placed inside the outer loop, causing the function to return after just one
# iteration. Also, the condition `if i > 0 or nums[i] == nums[i-1]` should use `and` instead of `or` to correctly skip duplicate starting elements.

def sum3_optimal(nums):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1
        target=-nums[i]
        while left<right:
            current_sum=nums[left]+nums[right]
            if current_sum==target:
                res.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif current_sum>target:
                right -= 1
            else:
                left+=1
    return res
print(sum3_optimal( nums = [-1,0,1,2,-1,-4]))