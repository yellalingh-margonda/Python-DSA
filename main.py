# Next Less Element (NLE)
arr=[3, 5, 3]
n = len(arr)
next_less = [n] * n
stack = []
for i in range(n - 1, -1, -1):
    print(f" for i:{i} stack {stack}")
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    next_less[i] = stack[-1] if stack else n
    print(f" for i:{i} next_less {next_less}")
    stack.append(i)
print(next_less)#[3,2,3]
#[2,2,3]
