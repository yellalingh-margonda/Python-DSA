res=[]
def right_view(node,level, res):
    if not node:
        return
    if level==len(res):# make sure to add the first node you encounter the node when you first arrvie to that level
        res.append(node)
    right_view(node.right, level+1, res)
    right_view(node.left, level+1, res)
    return res