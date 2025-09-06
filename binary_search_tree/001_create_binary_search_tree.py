class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

print("Inorder Traversal:", inorder(root))
# Output: [3, 5, 7, 10, 12, 15, 18]
