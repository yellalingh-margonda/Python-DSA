def matrix_rotation(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    res=[[None for _ in range(rows)] for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            res[col][cols-row-1]=matrix[row][col]
    return res
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix_rotation(matrix))

def matrix_rotation_inplace(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    for row in range(rows):
        for col in range(row+1, cols):
            matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
    for row in range(rows):
        matrix[row]=matrix[row][::-1]
    return matrix

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
