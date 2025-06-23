def partitioning_explicit_return(remaining, path=None):
    if path is None:
        path = []

    # Base case: if no remaining string, we found a valid partition
    if not remaining:
        return [path[:]] # Return a list containing the current partition

    all_partitions = [] # This will accumulate partitions found in this branch

    for i in range(1, len(remaining) + 1):
        prefix = remaining[:i]
        if prefix == prefix[::-1]:
            # If prefix is a palindrome, recurse
            # Pass a NEW path with the current prefix added
            # The recursive call will return a list of partitions from its branch
            path.append(prefix)
            results_from_subproblem = partitioning_explicit_return(remaining[i:], path)
            # Extend the overall list of partitions with the results from the subproblem
            all_partitions.extend(results_from_subproblem)
            path.pop()
    return all_partitions # Return all partitions found in this branch
print(partitioning_explicit_return(remaining='aab', path=[]))