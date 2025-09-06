
def next_smallest_ele(array):
    ans = []
    stack = []
    n = len(array)
    for i in range(2 * n - 1, -1, -1):
        while stack and stack[-1] >= array[i % n]:
            stack.pop()
        if i < n:
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
        stack.append(array[i % n])

    return ans[::-1]  # Reverse to match original order

print(next_smallest_ele([1, 3, 2, 4]))