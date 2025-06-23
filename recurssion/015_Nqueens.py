def is_valid(row, col, grid):
    for r in range(row):
        if grid[r][col]=='Q':
            return False
    for c in range(col):
        if grid[row][c] == 'Q':
            return False
    # Check upper-left diagonal
    # Iterate upwards and leftwards: (row-1, col-1), (row-2, col-2), etc.
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):  # Corrected range for upper-left
        if grid[r][c] == 'Q':
            return False

    # Check upper-right diagonal
    # Iterate upwards and rightwards: (row-1, col+1), (row-2, col+2), etc.
    # len(grid[0]) gives the number of columns
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, len(grid[0]))):  # Corrected range for upper-right
        if grid[r][c] == 'Q':
            return False
    return True

def Nqueens(n, grid=None,row=0, col=0,solutions=None):
    if grid==None:
        grid = [['.' for _ in range(n)] for _ in range(n)]
    if solutions is None:
        solutions = []
    if row == n:
        solution_copy = ["".join(r_item) for r_item in grid]  # Store as list of strings for cleaner output
        solutions.append(solution_copy)
        # DO NOT RETURN TRUE HERE. Allow backtracking to find other solutions.
        return solutions  #
    for c in range(n):
        if grid[row][c]=='.':
            if is_valid(row,c, grid):
                grid[row][c]='Q'
                Nqueens(n, grid,row+1, c, solutions)
                grid[row][c]='.'

    return solutions

soulitons=Nqueens(5)
print(soulitons[0])