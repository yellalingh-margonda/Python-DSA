def subset_sum(array, index=0, res=None, current_sum=0):
    """
    Computes all possible subset sums from the input array.

    Args:
        array (list): The input list of integers.
        index (int): Current index being considered.
        res (list): Accumulator for subset sums.
        current_sum (int): Sum accumulated so far.

    Returns:
        list: List of all subset sums.
    """
    if res is None:
        res = []

    if index == len(array):
        res.append(current_sum)
        return res

    # Include current element
    subset_sum(array, index + 1, res, current_sum + array[index])

    # Exclude current element
    subset_sum(array, index + 1, res, current_sum)

    return res

# ✅ Usage
result = subset_sum([1, 2, 3])
print(result)  # Output: [6, 3, 4, 1, 5, 2, 3, 0]


def subset_sum2(array, index=0,  current_sum=0):
    """
    Computes all possible subset sums from the input array.

    Args:
        array (list): The input list of integers.
        index (int): Current index being considered.
        res (list): Accumulator for subset sums.
        current_sum (int): Sum accumulated so far.

    Returns:
        list: List of all subset sums.
    """


    if index == len(array):
        return  [current_sum]
    sum_list=[]
    # Include current element
    left=subset_sum2(array, index + 1, current_sum + array[index])

    # Exclude current element
    right=subset_sum2(array, index + 1,  current_sum)
    sum_list.extend(left)
    sum_list.extend(right)

    return sum_list

# ✅ Usage
result = subset_sum2([1, 2, 3])
print(result)  # Output: [6, 3, 4, 1, 5, 2, 3, 0]

res=[]
def subset_sum3(array,index,res, sum=0 ):
    if res==None:
        res=[]
    if index==len(array):
        res.append(sum)
        return
    if index>len(array):
        return
    subset_sum3(array, index+1, res , sum+array[index])
    subset_sum3(array,index+1,res,sum)
    return
res=[]
subset_sum3([1,2,3],0,res)
print(res)
