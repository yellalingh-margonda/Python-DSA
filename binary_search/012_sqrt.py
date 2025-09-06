def sqrt_integer(n):
    if n < 2:
        return n

    start, end = 1, n // 2
    ans = 1

    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid  # store possible floor value
            start = mid + 1
        else:
            end = mid - 1

    return ans
