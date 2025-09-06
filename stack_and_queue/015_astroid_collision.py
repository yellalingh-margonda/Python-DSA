def astroid_correct(array):
    stack = []
    for asteroid in array:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            # Handle collisions with positive asteroids on the stack
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()

            # Check for final collision or a safe push
            if not stack or stack[-1] < 0:
                stack.append(asteroid)
            elif stack[-1] == abs(asteroid):
                stack.pop()
    return stack
print(astroid_correct([-5, -10, -5]))