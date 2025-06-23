def is_valid(grid,row,col, val):
    for i in range(9):
        if grid[i][col]==val or grid[row][i]==val:
            return False
    boxStartrow=(row//3)*3
    boxStartcol = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if grid[boxStartrow+r][boxStartcol+c]==val:
                return False
    return True

def solve(grid=None):
    if grid==None:
        grid=[[0 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                for num in range(1,10):
                    if is_valid(grid,row,col,num):
                        grid[row][col]=num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = solve(board)

if solved:
    for row in solved:
        print(row)
else:
    print("No solution exists")
