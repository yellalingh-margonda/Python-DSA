def twoSum(nums, target):
    hashmap = {}  # val:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i
    return

def twoSumflag(nums, target):
    hashmap = {}  # val:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return True
        hashmap[n] = i
    return False
