def reverse_array_recursive(array, left=0, right=None):
    """
    Recursively reverses the input array in-place.

    Args:
        array (list): The list to reverse.
        left (int): The starting index (default is 0).
        right (int): The ending index (default is len(array) - 1).

    Returns:
        list: The reversed array.
    """
    if right is None:
        right = len(array) - 1

    if left >= right:
        return array

    array[left], array[right] = array[right], array[left]
    return reverse_array_recursive(array, left + 1, right - 1)

# Example usage
print(reverse_array_recursive([1, 2, 3, 4, 5, 6]))

def reverse_array(array,n,i=0):
    """
    Recursively reverses the input array in-place.

    Args:
        array (list): The list to reverse.
        left (int): The starting index (default is 0).
        right (int): The ending index (default is len(array) - 1).

    Returns:
        list: The reversed array.
    """

    if i >= n//2:
        return array

    array[i], array[n-i-1] = array[n-i-1], array[i]
    return reverse_array(array, n,i+1)

print(reverse_array([1, 2, 3, 4, 5, 6], 6))

def parlindrom(string, n=None, i=0):
    if n is None:
        n = len(string)
    if i>=n/2:
        return True
    return string[i]==string[n-i-1] and parlindrom(string,n,i+1)

print(parlindrom('akba'))

