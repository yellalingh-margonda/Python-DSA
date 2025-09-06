def prev_smallest_ele(array):
    ans = []
    stack = []

    for i in range(len(array)):
        while stack and stack[-1] >= array[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(array[i])

    return ans  # Reverse to match original order

print(prev_smallest_ele([1, 3, 2, 4]))
