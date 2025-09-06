def invalid_parenthesis(string):
    mapping = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for ch in string:
        if ch not in mapping:  # ch is a closing bracket
            if not stack or mapping[stack.pop()] != ch:
                return False  # Invalid
        else:
            stack.append(ch)

    return len(stack) == 0  # Unmatched opening brackets → invalid
print(invalid_parenthesis('(]'))