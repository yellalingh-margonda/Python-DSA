def subsets_with_dup(arr):
    arr.sort()  # Required to handle duplicates
    result = []

    def backtrack(path, index):
        result.append(path[:])
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue  # Skip duplicates
            path.append(arr[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)
    return result
