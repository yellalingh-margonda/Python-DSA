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
values = [10, 5, 15, 3, 7, 12, 18]
root = None
for v in values:
    root = insert(root, v)


def find_right_most(root):
    if not root.right:
        return root
    return  find_right_most(root.right)

def helper(root):
    if not root.right:
        return root.left
    if not root.left:
        return root.right

    right=root.right
    left_most=find_right_most(root.left)
    left_most.right=right
    return root.left

def delete_node(root, val):
    if not root:
        return  root
    node=root
    while node:
        if node.val>val:
            if node.left and node.left.val==val:
                node.left=helper(node.left)
            else:
                node=node.left
        else:
            if node.right and node.right.val==val:
                node.right = helper(node.right)
            else:
                node=node.right
    return  root