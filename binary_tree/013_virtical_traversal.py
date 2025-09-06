map={}
max_level=[0]
min_level=[0]
def vertical_trase(node, level):
    if not node:
        return
    min_level[0] = min(min_level[0], level)
    max_level[0] = max(max_level[0], level)
    map[level]=map.get(level,[])+[node.val]
    vertical_trase(node.left, level-1)
    vertical_trase(node.right, level+1)
    return
res=[]
for i in range(min_level[0], max_level[0]+1):
    temp=map[i]
    res.append(sorted(temp))
