class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_value = postorder[-1]  # Last element in postorder is root
    root = TreeNode(root_value)  # Create the root node

    root_index_inorder = inorder.index(root_value)  # Find root in inorder

    # Elements for left subtree
    left_inorder = inorder[:root_index_inorder]
    right_inorder = inorder[root_index_inorder + 1:]

    # Elements for right subtree in postorder (excluding the root)
    right_postorder = postorder[len(left_inorder):-1]
    left_postorder = postorder[:-len(right_inorder) - 1]

    # Recursively build left and right subtrees
    root.left = buildTree(left_inorder, left_postorder)
    root.right = buildTree(right_inorder, right_postorder)

    return root


# Example usage
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
postorder = ['D', 'E', 'B', 'F', 'C', 'A']
root = buildTree(inorder, postorder)


# Function to print the tree in inorder (for verification)
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Print inorder traversal to verify
print(inorder_traversal(root))  # Should print inorder list ['D', 'B', 'E', 'A', 'F',]()_
