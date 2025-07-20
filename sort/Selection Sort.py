# Outer loop (i): Controls which position we're filling next with the correct element.
#
# Inner loop (j): Finds the index of the smallest element in the unsorted portion.
#
# ✅ After each outer loop iteration, the smallest unsorted element is placed in the correct spot (i.e., at position i).

def Selection_Sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

print(Selection_Sort([1,5,2,-1,-11]))