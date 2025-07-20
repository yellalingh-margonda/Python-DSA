#constant window
def max_sum(arr,k):

    n=len(arr)
    maxi=float('-inf')
    for i in range(n-k+1):
        current_sum=sum(arr[i:i+k])
        maxi=max(maxi,current_sum)
    return maxi


def max_sum2(arr,k):

    n=len(arr)
    maxi=float('-inf')
    for i in range(n-k+1):
        if i==0:
            current_sum=sum(arr[i:i+k])
        else:
            current_sum=current_sum-arr[i-1]+arr[i+k-1]
        maxi=max(maxi,current_sum)
    return maxi

#constant window
def max_sum3(arr,k):

    n=len(arr)
    maxi=float('-inf')
    l, r=0,k
    current_Sum = sum(arr[l:k-1])
    while r<n-1:#we cannot increase r beyond n-1,
        current_Sum=current_Sum-arr[l]
        l+-1
        r+=1
        current_sum=current_Sum+arr[r]
        maxi=max(maxi,current_sum)
    return maxi



def max_sum4(arr,k):

    n=len(arr)
    maxi=float('-inf')
    for i in range(n-k+1):
        if i==0:
            current_sum=sum(arr[i:i+k])
        else:
            current_sum=current_sum-arr[i-1]+arr[i+k-1]
        maxi=max(maxi,current_sum)
    return maxi
