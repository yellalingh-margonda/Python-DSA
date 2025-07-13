#'''The core idea of this approach is to find the length of the longest consecutive
# sequence in an unsorted array by treating each element as a potential starting point.
# For each element in the array, the algorithm repeatedly checks—using a linear search—whether
# the next consecutive number exists in the array. If it does, it continues increasing
# the candidate number and counting the length of the sequence. This process is repeated
# for all elements, and the maximum sequence length encountered is returned. Although simple,
# this method is inefficient due to the repeated linear searches,
# leading to an overall time complexity of O(n²).'''

def linear_search(arr,candidate):
    for ele in arr:
        if ele==candidate:
            return True
    return False
def longest_consicutive_sequence(arr):
    n=len(arr)
    maxi=float('-inf')
    for i in range(n):
        candidate=arr[i]
        count=0
        while linear_search(arr,candidate)==True:
              candidate = candidate+1
              count += 1
        maxi = max(count, maxi)
    return maxi
nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_consicutive_sequence(nums))

# The core idea of this approach is to first sort the array so that
# any consecutive numbers appear next to each other. After sorting,
# the algorithm iterates through the array, comparing each element
# with the last seen number. If the current number is exactly one more
# than the last, it extends the current consecutive sequence by incrementing the count.
# If the current number is a duplicate, it’s skipped without affecting the count.
# Otherwise, the count is reset to 1 for a new potential sequence.
# Throughout the iteration, the maximum sequence length (`longest`) is updated accordingly.
# This solution improves efficiency over a brute-force approach, achieving a time
# complexity of **O(n log n)** due to the sorting step.

def lengthOfLongestConsecutiveSequence(arr, n):
    longest=1
    last_number=float('-inf')
    count=0
    arr.sort()
    for i in range(n):
        if arr[i]-1==last_number:
            count+=1
            last_number=arr[i]
        elif arr[i]!=last_number:
            count=1
            last_number=arr[i]
        longest=max(longest,count)
    return longest

# The core idea of this approach is to use a set for O(1) lookups and identify
# the start of each consecutive sequence by checking if the previous number (ele - 1)
# is not in the set. For each such starting number, it counts the length of the consecutive
# sequence by incrementing next_num until the next number is no longer found in the set.
# This ensures each sequence is only counted once, and the maximum sequence length is updated during the process.
# This method is highly efficient with a time complexity of O(n)
# since each number is processed at most twice.
def longestConsecutive(nums) -> int:
    if len(nums) == 0:
        return 0
    s = set(nums)
    longest = -1
    for ele in s:
        if ele - 1 in s:
            continue

        next_num = ele + 1
        length = 1
        while next_num in s:
            length += 1
            next_num += 1

        longest = max(length, longest)
    return longest