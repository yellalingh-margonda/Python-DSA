# Outer Loop: Controls how many times we need to check the list.
#
# Inner Loop: Compares adjacent elements and swaps them if out of order.

def  bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=True
        if not swap:
            break
    return arr

print(bubble_sort([1,5,2,-1,-11]))