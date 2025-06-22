def combination_sum(array, target, path=None, current_sum=0, index=0):
    if path==None:
        path=[]
    if target==current_sum:
        return [path[:]]
    if index>=len(array) or current_sum>target:
        return None
    path.append(array[index])
    left = combination_sum(array,target,path,current_sum+array[index],index)
    path.pop()
    right= combination_sum(array,target,path,current_sum,index+1)
    return  left+right if left and right else right if right else left
print(combination_sum(array = [2,3,6,7], target = 7))


def com_sum(candidates, target, index=0, path=None):
    # Initialize path as an empty list only on the very first call.
    # This avoids the mutable default argument trap.
    if path is None:
        path = []

    # --- Base Cases ---
    # Base Case 1: If the target sum is exactly 0, we found a valid combination.
    # Return a list containing a copy of the current path.
    if target == 0:
        return [path[:]]

    # Base Case 2: If we've exhausted all candidates OR the target has become negative.
    # A negative target means we've overshot the sum with the current path.
    # Return an empty list, indicating no valid combinations from this point.
    if index >= len(candidates) or target < 0:
        return []

    # List to collect all combinations found from the current state (index, target)
    all_combinations_from_here = []

    # --- Recursive Step: Option 1 (Include current candidate) ---
    # Only attempt to include candidates[index] if it doesn't make the target negative
    # immediately. This is an optimization (pruning).
    if target >= candidates[index]:  # Check if current candidate can be included
        path.append(candidates[index])  # Add candidate to the current path

        # Recursive call: Reduce target, stay at same index (allowing re-use of candidate)
        results_with_current = com_sum(candidates, target - candidates[index], index, path)
        all_combinations_from_here.extend(results_with_current)  # Add all combinations from this branch

        path.pop()  # Backtrack: Remove the candidate to prepare for the "exclude" branch

    # --- Recursive Step: Option 2 (Exclude current candidate) ---
    # Always explore the option of not including the current candidate and moving to the next one.
    # This should NOT be nested inside the "include" condition.
    results_without_current = com_sum(candidates, target, index + 1, path)
    all_combinations_from_here.extend(results_without_current)  # Add all combinations from this branch

    # Return all combinations found from this current function call's perspective
    return all_combinations_from_here

def combination_sum(index, sum, target, path, array):
    if index==len(array):
        if sum==target:
            return [path[:]]
        return None
    path.append(array[index])
    result=combination_sum(index+1, sum+array[index],target, path,array )
    if result:
        return result
    path.pop()  # backtrack
    result = combination_sum(index + 1, sum, target, path, array)
    if result:
        return  result
    return None

arr = [2, 4, 6, 8]
target = 10
result = combination_sum(0, 0, target, [], arr)
print(result)  # Might return something like [[2, 4, 4]] or first match



def combination_sumall(index, sum, target, path, array):
    if index==len(array):
        if sum==target:
            return [path[:]]
        return []
    if sum>target:
        return []
    path.append(array[index])
    left=combination_sumall(index+1, sum+array[index],target, path,array )
    path.pop()  # backtrack
    right = combination_sumall(index + 1, sum, target, path, array)
    return left+right
def find_all_combinations(array, target):
    return combination_sumall(0, 0, target, [], array)
arr = [2, 4, 6, 8]
target = 10
print(find_all_combinations(arr, target))
# Output: All unique combinations where the sum is 8

def combination_sumcount(index, current_sum, target, array):
    if current_sum == target:
        return 1
    if current_sum > target or index == len(array):
        return 0

    # Include the current element
    count_including = combination_sumcount(index + 1, current_sum + array[index], target, array)

    # Exclude the current element
    count_excluding = combination_sumcount(index + 1, current_sum, target, array)

    return count_including + count_excluding