def max_sum_sub(arr):
    n = len(arr)
    prefix_sum = [arr[0]]

    # Build prefix sum array
    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + arr[i])

    print("Prefix sum:", prefix_sum)

    maxi = float('-inf')

    # Try all subarrays
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                sub_sum = prefix_sum[j]
            else:
                sub_sum = prefix_sum[j] - prefix_sum[i - 1]
            maxi = max(maxi, sub_sum)
        print(f"Max till index {i}:", maxi)

    return maxi


# Test
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Max subarray sum:", max_sum_sub(nums))

#Kadane’s '''Algorithm is an efficient method to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers, using a single pass with linear time complexity
# 𝑂(𝑛) O(n). It works by iterating through the array while maintaining two variables: current_sum, which keeps track of the maximum sum ending at the current index, and max_sum, which stores the overall maximum found so far. At each step, current_sum is updated as the maximum of the current element or the sum of the current element and the previous current_sum, effectively deciding whether to start a new subarray or continue the current one. max_sum is updated if current_sum exceeds it. This allows the algorithm to handle both positive and negative numbers efficiently.'''





def kadane_algorithm(arr):
    if not arr:
        return 0  # or float('-inf') depending on requirements

    current_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
print(kadane_algorithm([5,4,-1,7,8]))

