def next_smallest_ele(array):
    ans = []
    stack = []

    for i in range(len(array) - 1, -1, -1):
        while stack and stack[-1] >= array[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(array[i])

    return ans[::-1]  # Reverse to match original order

print(next_smallest_ele([1, 3, 2, 4]))
