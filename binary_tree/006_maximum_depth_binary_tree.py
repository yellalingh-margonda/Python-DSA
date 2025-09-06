def maxmim_depth(node):
    if not node:
        return 0
    left=maxmim_depth(node.left)
    right=maxmim_depth(node.right)
    return 1+max(left,right)