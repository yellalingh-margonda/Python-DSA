def permutations(array, used=None, path=None):
    if used is None:
        used = [0] * len(array)  # Dynamically sized map
    if path is None:
        path = []

    if len(path) == len(array):
        return [path[:]]  # Base case: one full permutation

    result = []
    for i in range(len(array)):
        if used[i] == 0:
            used[i] = 1
            path.append(array[i])

            result += permutations(array, used, path)

            path.pop()
            used[i] = 0

    return result
