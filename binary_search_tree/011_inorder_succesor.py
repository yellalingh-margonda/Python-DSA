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


def inorder_sucessor(root, p):
    succesor=None
    node=root
    while node:
        if node.val <= p.val:
            node=node.right
        else:
            succesor=node
            node=node.left
    return succesor