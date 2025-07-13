def largest_ele(array):
    largest=array[0]
    for ele in array:
        if ele>=largest:
            largest=ele
    return largest
def second_largest(array):
    largest=largest_ele(array)
    slarg=-1
    for ele in array:
        if ele >slarg and ele!= largest:
            slarg=ele
    return slarg
array = [10, 20, 4, 45, 99, 45]
print(second_largest(array))  # Output: 45

def second_larget_opt(array):
    largest = array[0]
    slarg = -1
    for ele in array:
        if ele > largest:
            slarg = largest
            largest = ele
        elif ele < largest:
            if ele > slarg:
                slarg = ele
        else:
            continue
    return slarg
array = [10, 20, 4, 45, 99, 45]
print(second_larget_opt(array))  # Output: 45

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
print(is_sorted([1, 2, 3, 4]))  # True
print(is_sorted([1, 3, 2, 4]))  # False
print(is_sorted([]))           # True (an empty list is considered sorted)
print(is_sorted([5]))          # True (a single-element list is sorted)


def unique_elements(array):
        i, j = 0, 1
        while j < len(array):
            if array[j] != array[i]:
                array[i+1] = array[j]
                i = i+1
                j = j+1
            else:
                j = j+1
        return i+1

print(unique_elements([1, 1, 2, 2, 3, 4, 4, 5,5]))  # [1, 2, 3, 4, 5]
print(unique_elements([]))                      # []
print(unique_elements([7, 7, 7]))               # [7]
