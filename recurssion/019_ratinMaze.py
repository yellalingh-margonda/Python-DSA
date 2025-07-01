def ratinmaze(n,visited=None, dirs=None,path=None, row=0, col=0):

    if path is None:
        path=[]
    if visited==None:
        visited=[[False for _ in range(n)] for _ in range(n)]
        # 2. Rat is out of bounds or already visited
    if not (0 <= row < n and 0 <= col < n) or visited[row][col]:
            return []  # No path from this point, return an empty list
    if dirs is None:
        dirs=[(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
    if row==n-1 and col==n-1:
        return ["".join(path)]
    paths_at_this_branch=[]
    visited[row][col] = True
    for dr,dc , move in dirs:
        next_row, next_col= row+dr,col+dc
        if  (0 <= next_row < n and 0 <= next_col < n) and not  visited[next_row][next_col]:
            path.append(move)
            sub_res=ratinmaze(n, visited, dirs,path,next_row, next_col)
            path.pop()
            paths_at_this_branch.extend(sub_res)
    visited[row][col] = False
    return paths_at_this_branch
all_found_paths = ratinmaze(3)
print(all_found_paths)