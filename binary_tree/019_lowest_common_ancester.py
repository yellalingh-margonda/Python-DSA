def lowest_common_ancester(node,p,q):
    if not node:
        return None
    if node==p or node==q:
        return node
    left = lowest_common_ancester(node.left, p, q)
    right = lowest_common_ancester(node.right, p, q)
    if left and right:
        return node
    return left if left else right
