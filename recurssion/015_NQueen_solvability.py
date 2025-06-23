def is_valid(row, col, grid):
    for r in range(row):
        if grid[r][col] == 'Q':
            return False
    for c in range(col):
        if grid[row][c] == 'Q':
            return False
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if grid[r][c] == 'Q':
            return False
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, len(grid[0]))):
        if grid[r][c] == 'Q':
            return False
    return True

def is_Nqueens_solvable(n, grid=None, row=0):
    if grid is None:
        grid = [['.' for _ in range(n)] for _ in range(n)]

    if row == n:
        return True  # Found a valid solution

    for c in range(n):
        if is_valid(row, c, grid):
            grid[row][c] = 'Q'
            if is_Nqueens_solvable(n, grid, row + 1):
                return True  # Early exit on first valid solution
            grid[row][c] = '.'

    return False  # No solution found for this row

# Example usage:
print(is_Nqueens_solvable(5))  # True
print(is_Nqueens_solvable(2))  # False
