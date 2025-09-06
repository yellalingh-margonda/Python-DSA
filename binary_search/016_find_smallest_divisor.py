def shipWithinDays(weights, days):
    def possible(array, limit, capacity):
        current_capacity = 0
        d = 1
        for w in array:
            if current_capacity + w > capacity:
                d += 1
                current_capacity = 0
            current_capacity += w
        return d <= limit

    left, right = max(weights), sum(weights)
    ans = right  # keep track of best so far

    while left <= right:
        mid = (left + right) // 2
        if possible(weights, days, mid):
            ans = mid  # store valid answer
            right = mid - 1  # try smaller
        else:
            left = mid + 1  # need larger

    return ans
