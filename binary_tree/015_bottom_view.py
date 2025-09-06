def bottom_view(node, x,y):
    if not node:
        return
    if x not in map or y>map[x][0]: # this condition makes sure that we take either new value in the colum or earliest value of y ie. in the row, since want to see the top view we should most shallow element
        map[x]=(y, node.val)
    bottom_view(node.left, x-1,y+1)
    bottom_view(node.right, x +1, y + 1)
    return
map = {}
bottom_view(root, 0, 0)
result = [map[x][1] for x in sorted(map)]
print(result)
