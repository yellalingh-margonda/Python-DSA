class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Insert function for BST
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root
