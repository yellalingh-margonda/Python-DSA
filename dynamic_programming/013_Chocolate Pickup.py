def max_chocolate(row, col1, col2, grid):
    # Base cases
    if col1 < 0 or col1 >= len(grid[0]) or col2 < 0 or col2 >= len(grid[0]):
        return float('-inf')

    # If we're at the last row
    if row == len(grid) - 1:
        if col1 == col2:
            return grid[row][col1]
        else:
            return grid[row][col1] + grid[row][col2]

    # Recursive case
    max_choco = float('-inf')
    for d1 in [-1, 0, 1]:
        for d2 in [-1, 0, 1]:
            next_col1 = col1 + d1
            next_col2 = col2 + d2
            temp = max_chocolate(row + 1, next_col1, next_col2, grid)
            if col1 == col2:
                temp += grid[row][col1]
            else:
                temp += grid[row][col1] + grid[row][col2]
            max_choco = max(max_choco, temp)

    return max_choco
grid = [
    [3, 1, 1],
    [2, 5, 1],
    [1, 5, 5],
    [2, 1, 1]
]

# Start from row 0, columns 0 and len(grid[0]) - 1
result = max_chocolate(0, 0, len(grid[0]) - 1, grid)
print(result)  # Output should be 24

def max_chocolate_memo(row, col1, col2, grid,dp=None):
    if dp is None:
        dp=[[[float('-inf') for _ in range(len(grid[0]))] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Base cases
    if col1 < 0 or col1 >= len(grid[0]) or col2 < 0 or col2 >= len(grid[0]):
        return float('-inf')

    # If we're at the last row
    if row == len(grid) - 1:
        if col1 == col2:
            return grid[row][col1]
        else:
            return grid[row][col1] + grid[row][col2]
    if dp[row][col1][col2] != float('-inf'):
        return dp[row][col1][col2]
    # Recursive case
    max_choco = float('-inf')
    for d1 in [-1, 0, 1]:
        for d2 in [-1, 0, 1]:
            next_col1 = col1 + d1
            next_col2 = col2 + d2
            temp = max_chocolate_memo(row + 1, next_col1, next_col2, grid,dp)
            if col1 == col2:
                temp += grid[row][col1]
            else:
                temp += grid[row][col1] + grid[row][col2]
            max_choco = max(max_choco, temp)
    dp[row][col1][col2]=max_choco
    return dp[row][col1][col2]

# Start from row 0, columns 0 and len(grid[0]) - 1
result = max_chocolate_memo(0, 0, len(grid[0]) - 1, grid)
print(result)  # Output should be 24

def max_chocolate_tabulation(grid,dp=None):
    rows, cols=len(grid), len(grid[0])
    if dp is None:
        dp=[[[float('-inf') for _ in range(len(grid[0]))] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for c1 in range(cols):
        for c2 in range(cols):
            if c1 == c2:
                dp[rows][c1][c2]=grid[len(grid)-1][c1]
            else:
                dp[rows][c1][c2]=grid[len(grid)-1][c1]+grid[len(grid)-1][c2]
    for row in range(rows - 2,-1,-1):
        for c1 in range(cols):
            for c2 in range(cols):
                max_choco = float('-inf')
                for d1 in [-1, 0, 1]:
                    for d2 in [-1, 0, 1]:
                        next_col1 = c1 + d1
                        next_col2 = c2 + d2
                        if 0 <= next_col1 < cols and 0 <= next_col2 < cols:
                            temp = dp[row + 1][next_col1][next_col2]
                            if c1 == c2:
                                temp += grid[row][c1]
                            else:
                                temp += grid[row][c1] + grid[row][c2]
                            max_choco = max(max_choco, temp)
                dp[row][c1][c2]=max_choco
        return dp[0][0][cols-1]

# Start from row 0, columns 0 and len(grid[0]) - 1
result = max_chocolate_memo(0, 0, len(grid[0]) - 1, grid)
print(result)  # Output should be 24
