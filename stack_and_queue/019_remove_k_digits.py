def removeKdigits(string, k):
    stack = []
    count = 0

    for ch in string:
        digit = int(ch)
        while stack and stack[-1] > digit and count < k:
            stack.pop()
            count += 1
        stack.append(digit)

    # Remove remaining digits from end if needed
    while count < k:
        stack.pop()
        count += 1

    # Convert stack to string, remove leading zeros
    result = ''.join(map(str, stack)).lstrip('0')

    return result if result else '0'
print(removeKdigits("10200", 1))   # Output: "200"
print(removeKdigits("1432219", 3)) # Output: "1219"
print(removeKdigits("10", 2))      # Output: "0"
