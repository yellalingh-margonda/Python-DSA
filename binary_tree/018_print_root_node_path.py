def node_path(node, path,ele):
    if not node:
        return False
    path.append(node.val)
    if node.val==ele:
         return True
    left = node_path(node.left, path, ele)
    right = node_path(node.right, path, ele)
    if not left and not right:
        path.pop()
    return left or right

# Example usage
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

path = []
node_path(root, path, 5)
print(path)  # Output: [1, 2, 5]
