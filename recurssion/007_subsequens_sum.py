def sub_sum(array, target, path=None, current_total=0, index=0):
    """
    Recursively finds all subsequences of the input array whose elements sum to the target value.

    Args:
        array (list): The input list of integers.
        target (int): The desired sum.
        path (list): Current combination being explored.
        current_total (int): Running total of the current path.
        index (int): Current index in the array.

    Returns:
        list: A list of valid subsequences whose sum equals the target.
    """
    if path is None:
        path = []

    if current_total == target:
        return [path[:]]

    if index >= len(array) or current_total > target:
        return []

    # Include current element
    path.append(array[index])
    include = sub_sum(array, target, path, current_total + array[index], index + 1)

    # Exclude current element
    path.pop()
    exclude = sub_sum(array, target, path, current_total, index + 1)

    return include + exclude

# Example usage
print(sub_sum([1, 2, 1], 2))

def sub_single_sum(array, target, path=None, current_total=0, index=0):
    """
    Recursively finds all subsequences of the input array whose elements sum to the target value.

    Args:
        array (list): The input list of integers.
        target (int): The desired sum.
        path (list): Current combination being explored.
        current_total (int): Running total of the current path.
        index (int): Current index in the array.

    Returns:
        list: A list of valid subsequences whose sum equals the target.
    """
    if path is None:
        path = []

    if current_total == target:
        return [path[:]]

    if index >= len(array) or current_total > target:
        return []

    # Include current element
    path.append(array[index])
    include = sub_single_sum(array, target, path, current_total + array[index], index + 1)
    if include:
        return include
    # Exclude current element
    path.pop()
    exclude = sub_single_sum(array, target, path, current_total, index + 1)
    if exclude:
        return exclude
    return []

# Example usage
print(sub_single_sum([1, 2, 1], 2))

def subseq_sum_flag(array, target, index=0, path=None, current_sum=0):
    if path==None:
        path=[]
    if current_sum==target:
        return path
    if index>=len(array) or  current_sum > target:
        return False
    path.append(array[index])
    if subseq_sum_flag(array, target, index+1, path, current_sum+array[index]):
        return path
    path.pop()
    if subseq_sum_flag(array, target, index + 1, path, current_sum):
        return path
    return None
# Example Usage:
my_array = [3, 34, 4, 12, 5, 2]

target_sum_1 = 9
result_1 = subseq_sum_flag(my_array, target_sum_1)
print(f"Subsequence for target {target_sum_1}: {result_1}")


def sub_seq_count(array, target, index=0, current_sum=0):
    # Base Case 1: Target sum achieved. This path contributes 1 to the count.
    if current_sum == target:
        return 1

    # Base Case 2: Exhausted array OR current_sum exceeded target.
    # If we've run out of elements or gone over the target, this path yields no solution.
    # The 'current_sum > target' check is an important optimization for positive numbers.
    if index >= len(array) or current_sum > target:  # <-- Corrected condition
        return 0

    # Recursive Step: Explore two possibilities
    count = 0

    # Option 1: Include the current element
    count += sub_seq_count(array, target, index + 1, current_sum + array[index])

    # Option 2: Exclude the current element
    count += sub_seq_count(array, target, index + 1, current_sum)

    return count
#key to observe is that when we are counting then we are not passing count as an parameter, because count value scope will be limited to the fucntion its in,
#when we are find paths we can pass variable path