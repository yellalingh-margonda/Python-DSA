#The function reArrangeSign rearranges a given array so that all positive integers occupy even indices (0, 2, 4, ...) and all negative integers occupy odd indices (1, 3, 5, ...), ensuring an alternating sign pattern throughout the result. It does this by initializing a new result array res with the same length and two pointers: pos for the next available even index and neg for the next available odd index. As it loops through the input array, if an element is positive, it is placed at the current even index (pos), and pos is incremented by 2; if it’s negative, it is placed at the current odd index (neg), and neg is incremented by 2. This guarantees that the output alternates between positive and negative numbers, while preserving the relative order of numbers with the same sign.

def reArrangeSign(arr,n):
    res=[None]*len(arr)
    pos=0
    neg=1
    for i in range(n):
        if arr[i]>0:
            res[pos]=arr[i]
            pos+=2
        else:
            res[neg] = arr[i]
            neg+=2
    return res

arr = [-1, -2, -3, 4, 5, 6]
print(reArrangeSign(arr,6))
