def spiralPathMatrix(matrix, n, m):
    # Initialize boundaries.
    # top: starting row index
    # bottom: ending row index
    # left: starting column index
    # right: ending column index
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    res = []

    # Loop until all elements are traversed
    while top <= bottom and left <= right:
        # 1. Traverse Right (Top row)
        # Iterate from 'left' to 'right' across the 'top' row
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1  # Move 'top' boundary down

        # 2. Traverse Down (Rightmost column)
        # Check if there are still rows to traverse
        if top <= bottom:  # Important check for single row matrices
            # Iterate from 'top' to 'bottom' down the 'right' column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move 'right' boundary left

        # 3. Traverse Left (Bottom row)
        # Check if there are still rows AND columns to traverse
        if left <= right and top <= bottom:  # Important check for single column/row matrices
            # Iterate from 'right' to 'left' across the 'bottom' row
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1  # Move 'bottom' boundary up

        # 4. Traverse Up (Leftmost column)
        # Check if there are still rows AND columns to traverse
        if top <= bottom and left <= right:  # Important check for single row/column matrices
            # Iterate from 'bottom' to 'top' up the 'left' column
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Move 'left' boundary right

    return res