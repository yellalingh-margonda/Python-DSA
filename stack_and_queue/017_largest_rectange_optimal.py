def largest_hist(arr):
    n = len(arr)
    stack = []
    maxi = 0

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            index = stack.pop()
            height = arr[index]
            width = i if not stack else i - stack[-1] - 1
            maxi = max(maxi, height * width)
        stack.append(i)

    # Process remaining items in the stack
    while stack:
        index = stack.pop()
        height = arr[index]
        width = n if not stack else n - stack[-1] - 1
        maxi = max(maxi, height * width)

    return maxi

# Example usage
heights = [2, 1, 5, 6, 2, 3]
print(largest_hist(heights))  # Output: 10

