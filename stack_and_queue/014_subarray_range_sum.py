def subSrrayRangeSum(array):
    n=len(array)
    prev_less=[-1]*n
    next_less=[n]*n
    stack=[]
    for i in range(n):
        while stack and array[stack[-1]]>array[i]:
            stack.pop()
        prev_less[i]=stack[-1] if stack else -1
        stack.append(i)
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and array[stack[-1]]>=array[i]:
            stack.pop()
        next_less[i]=stack[-1] if stack else n
        stack.append(i)

    prev_greter = [-1] * n
    next_greter = [n] * n
    stack = []
    for i in range(n):
        while stack and array[stack[-1]] < array[i]:
            stack.pop()
        prev_greter[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and array[stack[-1]] <= array[i]:
            stack.pop()
        next_greter[i] = stack[-1] if stack else n
        stack.append(i)
        # Calculate result
    result = 0
    for i in range(n):
        left = i - prev_less[i]
        right = next_less[i] - i
        result = (result + array[i] * left * right)
    result1 = 0
    for i in range(n):
        left = i - prev_greter[i]
        right = next_greter[i] - i
        result1 = (result1 + array[i] * left * right)
    return result1-result
print(subSrrayRangeSum([1, 2, 3]))  # Output: 4
