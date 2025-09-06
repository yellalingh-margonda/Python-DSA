class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder[0]  # First element in preorder is root
    root = TreeNode(root_value)  # Create the root node

    root_index_inorder = inorder.index(root_value)  # Find root in inorder

    # Elements for left subtree
    left_inorder = inorder[:root_index_inorder]
    right_inorder = inorder[root_index_inorder + 1:]

    # Elements for right subtree
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    # Recursively build left and right subtrees
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root


# Example usage
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
root = buildTree(preorder, inorder)


# Function to print the tree in inorder (for verification)
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Print inorder traversal to verify
print(inorder_traversal(root))  # Should print inorder list ['D', 'B', 'E', 'A', 'F', 'C']
