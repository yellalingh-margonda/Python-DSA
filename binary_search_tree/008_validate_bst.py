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


def validate_bst(node, left=None, right=None):
    if node is None:
        return True
    if not left:
        left=float('-inf')
    if not right:
        right=float('inf')
    if left<node.val<right:
        return True
    return validate_bst(node.left, left, node.val) and validate_bst(node.right, node.val, right)
