def left_height(node):
    height=0
    while node:
        height+=1
        node=node.left
    return height

def right_height(node):
    height=0
    while node:
        height+=1
        node=node.right
    return height

def count(node):
    if not node:
        return 0
    lh=left_height(node.left)
    rh=right_height(node.right)
    if lh==rh:
        return (1 << lh) - 1
    return 1+count(node.left)+count(node.right)
