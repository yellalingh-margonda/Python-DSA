def set_zero(arr):
    m=len(arr)
    n=len(arr[0])
    res=[]
    for i in range(m):
        for j in range(n):
            if arr[i][j]==0:
                res.append((i,j))
    for i, j in res:
        for row in range(m):
            arr[row][j]=0
        for col in range(n):
            arr[i][col]=0
    return arr
def set_zero_better(matrix):
    n=len(matrix)
    m=len(matrix[0])
    col=[0]*m
    row=[0]*n
    for r in range(n):
        for c in range(m):
            if matrix[r][c]==0:
                col[c]=1
                row[r]=1
    for r in range(n):
        for c in range(m):
            if col[c] == 1 or row[r]==1:
                matrix[r][c]=0
    return matrix

def setZeroes(matrix):
        n = len(matrix)
        m = len(matrix[0])
        first_row = 1
        first_col = 1

        # Check if first row has any zero
        for i in range(m):
            if matrix[0][i] == 0:
                first_row = 0

        # Check if first column has any zero
        for i in range(n):
            if matrix[i][0] == 0:
                first_col = 0

        # Use first row and column as markers
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # Update the inner matrix based on markers
        for r in range(1, n):
            for c in range(1, m):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Update first row if needed
        if first_row == 0:
            for i in range(m):
                matrix[0][i] = 0

        # Update first column if needed
        if first_col == 0:
            for i in range(n):
                matrix[i][0] = 0