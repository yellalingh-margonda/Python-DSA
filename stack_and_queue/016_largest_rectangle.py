def largest_hist(arr):
    n=len(arr)
    prev_less=[-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        prev_less[i]=stack[-1] if stack else -1
        stack.append(i)
    next_less=[n]*n
    stack=[]
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        next_less[i]=stack[-1] if stack else n
        stack.append(i)

    maxi=float('-inf')
    for i in range(n):
        maxi=max(maxi, arr[i]*(next_less[i]-prev_less[i]-1))
    return  maxi
heights = [2,1,5,6,2,3]
print(largest_hist(heights))