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
input=[[0,1],[1,0]]
temp=input[0]
maxi= largest_hist(temp)
for i in range(1, len(input)):
    for j in range(len(temp)):
        temp[j]=temp[j]+input[i][j] if input[i][j] == 1 else 0
    maxi=max(maxi, largest_hist(temp))
print(maxi)