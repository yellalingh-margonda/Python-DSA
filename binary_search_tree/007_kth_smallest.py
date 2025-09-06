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

def kth_smallest(node, k):
    def inorder(node):
        if not node:
            return None
        # Traverse left
        val = inorder(node.left)
        if val is not None:
            return val

        # Visit current node
        counter[0] += 1
        if counter[0] == k:
            return node.val

        # Traverse right
        return inorder(node.right)

    counter = [0]
    return inorder(node)
def kth_smallest(node, k):
    def inorder(node, count):
        if not node:
            return count, None

        # Traverse left
        count, val = inorder(node.left, count)
        if val is not None:
            return count, val

        # Visit current node
        count += 1
        if count == k:
            return count, node.val

        # Traverse right
        return inorder(node.right, count)

    _, result = inorder(node, 0)
    return result
