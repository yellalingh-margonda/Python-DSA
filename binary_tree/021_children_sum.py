def children_sum(node):
    if not node:
        return node
    child = node.left.data if node.left else 0
    child += node.right.data if node.right else 0
    #while going down either adjust the child nodes or the root nodes, based on which ever is greater
    # root is grater assign the root value to child, if child is greater assign the child value to root
    if node.data>child:
        if node.left:
            node.left.data = child
        if node.right:
            node.right.data = child
    elif node.data <= child:
        node.data=child
    children_sum(node.left)
    children_sum(node.right)
    total=0
    if node.left:
        total+=node.left.data
    if node.right:
        total+=node.right.data
    node.data=total
    return




