class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def maxPathSum(root):
    maxi = [float('-inf')]

    def maxi_Sum(node):
        if not node:
            return 0
        left = max(0, maxi_Sum(node.left))
        right = max(0, maxi_Sum(node.right))
        maxi[0] = max(maxi[0], left + right + node.val)
        return max(left, right) + node.val

    maxi_Sum(root)
    return maxi[0]

# Build a tree with all negative values
root = TreeNode(-10)
root.left = TreeNode(-20)
root.right = TreeNode(-30)

print(maxPathSum(root))  # Output should be -10
