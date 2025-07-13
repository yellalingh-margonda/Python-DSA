def subarray_sum(array,k):
    n= len(array)
    count=0
    for i in range(n):
        for j in range(i, n):
           val = sum(array[i:j+1])
           count = count + 1 if val % k == 0 else count
    return count
array= [4,5,0,-2,-3,1]
k = 5
subarray_sum(array, k)



def longest_subarray(array, k):
    n = len(array)
    maxi=float('-inf')
    for i in range(n):
        for j in range(i, n):
            val = sum(array[i:j + 1])
            if val % k == 0:
                maxi=max(j-i+1,maxi)
    return maxi

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    prefix_sum=[a[0]]
    n=len(a)
    maxi=float('-inf')
    for i in range(1,n):
        prefix_sum.append(prefix_sum[i-1]+a[i])
    prefix_map={}
    for i in range(n):
        if prefix_sum[i] not in prefix_map:
            prefix_map[prefix_sum[i]]=i
        if prefix_sum[i]==k:
            maxi=max(maxi, i+1)
        if prefix_sum[i]-k in prefix_map:
                maxi= max(maxi,i-prefix_map[prefix_sum[i]-k])
    return maxi if maxi!= float('-inf') else -1


def longestSubarrayWithSumKonlypositive(a: [int], k: int) -> int:
    prefix_sum=[a[0]]
    n=len(a)
    maxi=float('-inf')
    for i in range(1,n):
        prefix_sum.append(prefix_sum[i-1]+a[i])
    prefix_map={}
    for i in range(n):
        if prefix_sum[i] not in prefix_map:
            prefix_map[prefix_sum[i]]=i
        if prefix_sum[i]==k:
            maxi=max(maxi, i+1)
        if prefix_sum[i]-k in prefix_map:
                maxi= max(maxi,i-prefix_map[prefix_sum[i]-k])
    return maxi if maxi!= float('-inf') else -1



def longest_subarray_sum(arr, k):
    n = len(arr)
    l = 0
    sub_sum = 0
    max_len = 0

    for r in range(n):
        sub_sum += arr[r]

        while l <= r and sub_sum > k:
            sub_sum -= arr[l]
            l += 1

        if sub_sum % k == 0:
            max_len = max(max_len, r - l + 1)

    return max_len if max_len > 0 else -1