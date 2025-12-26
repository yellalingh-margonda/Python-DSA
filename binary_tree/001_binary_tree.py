class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Testing 
def insert_node(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root


def create_binary_tree(nums):
    if not nums:
        return None

    root = Node(nums[0])
    for ele in nums[1:]:
        insert_node(root, ele)
    return root


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)


# Test
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root = create_binary_tree(nums)
print("In-order Traversal:")
inorder_traversal(tree_root)
