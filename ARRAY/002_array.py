def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n  # Handle k > n

    for _ in range(k):
        # Save the first element
        temp = arr[0]

        # Shift all elements to the left by 1
        for i in range(1, n):
            arr[i - 1] = arr[i]

        # Put the first element at the end
        arr[n - 1] = temp

    return arr

def rev(array):
    n=len(array)
    for i in range(n//2):
        array[i],array[n-1-i]=array[n-1-i],array[i]
    return  array


def rev(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

def rotateArray_optimal(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n  # Handle cases where k > n

    # Step 1: Reverse the whole array
    rev(arr, 0, n - 1)

    # Step 2: Reverse the first k elements
    rev(arr, 0, k - 1)

    # Step 3: Reverse the remaining n - k elements
    rev(arr, k, n - 1)

    return arr

# Example
nums = [1, 2, 3, 4, 5, 6, 7]
print(rotateArray_optimal(nums, 3))  # Output: [5, 6, 7, 1, 2, 3, 4]

def rev(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

def rotateArray_left(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n  # Handle k > n

    # Step 1: Reverse first k elements
    rev(arr, 0, k - 1)

    # Step 2: Reverse the remaining elements
    rev(arr, k, n - 1)

    # Step 3: Reverse the entire array
    rev(arr, 0, n - 1)

    return arr


from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    n, z = len(nums), 0

    # Find the first zero
    while z < n and nums[z] != 0:
        z += 1

    # nz starts just after z
    nz = z + 1

    while nz < n:
        if nums[nz] != 0:
            # Swap non-zero at nz with zero at z
            nums[nz], nums[z] = nums[z], nums[nz]
            z += 1  # Move z forward to next zero position
        nz += 1

def linearSearchFirst(array, target):

    for i in range(len(array)):
        if target==array[i]:
            return i
    return -1


def linearSearchLast(array, target):
    for i in range(len(array)-1,-1,-1):
        if target == array[i]:
            return i
    return -1


def union_sorted_arrays(array1, array2):
    i, j = 0, 0
    m, n = len(array1), len(array2)
    union_list = []
    last = None

    while i < m and j < n:
        if array1[i] < array2[j]:
            if array1[i] != last:
                union_list.append(array1[i])
                last = array1[i]
            i += 1
        elif array1[i] > array2[j]:
            if array2[j] != last:
                union_list.append(array2[j])
                last = array2[j]
            j += 1
        else:  # array1[i] == array2[j]
            if array1[i] != last:
                union_list.append(array1[i])
                last = array1[i]
            i += 1
            j += 1

    while i < m:
        if array1[i] != last:
            union_list.append(array1[i])
            last = array1[i]
        i += 1

    while j < n:
        if array2[j] != last:
            union_list.append(array2[j])
            last = array2[j]
        j += 1

    return union_list

