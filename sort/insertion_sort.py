def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        key = arr[i]       # Element to be inserted
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at correct position
        arr[j + 1] = key
    return arr

print(insertion_sort([1,5,2,-1,-11]))