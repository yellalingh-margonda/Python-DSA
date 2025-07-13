def missing_number(arr):
    n = len(arr) + 1
    for i in range(1, n + 1):
        found = False
        for j in range(len(arr)):
            if arr[j] == i:
                found = True
                break
        if not found:
            return i

def missing_number_hash(arr):
    n = len(arr) + 1  # Since one number from 1 to n is missing
    hash_arr = [0] * (n + 1)  # Extra index to include n

    for ele in arr:
        hash_arr[ele] = 1

    for i in range(1, n + 1):
        if hash_arr[i] == 0:
            return i

    return -1  # If nothing is missing (should not happen if input is valid)
def missing_number_xor(arr):
    n = len(arr) + 1  # Since one number from 1 to n is missing
    xor_all = 0
    xor_arr = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all elements in the array
    for num in arr:
        xor_arr ^= num

    # XORing these gives the missing number
    return xor_all ^ xor_arr

def max_consicutive_ones(nums):
    maxi=0
    curr_count=0
    for i in nums:
        if i ==1:
            curr_count+=1
            maxi = max(maxi, curr_count)
        else:
            curr_count=0
    return maxi
def findNonRepeating(arr):
    hash_set={}
    for ele in arr:
        hash_set[ele]=hash_set.get(ele, 0)+1
    res=[]
    for ele in arr:
        if hash_set[ele]==1:
            res.append(ele)
    return res