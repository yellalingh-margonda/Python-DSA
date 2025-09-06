maxi=[0]
def diameterof_tree(node):
    if not node:
        return 0
    left= diameterof_tree(node.left)
    right=diameterof_tree(node.right)
    maxi[0]=max(maxi[0], left+right)
    return 1+max(left,right)

