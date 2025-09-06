from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def print_tree_level_by_level(root):
    """
    Prints the binary tree level by level (Breadth-First Search traversal).
    'N' is used as a placeholder for None (missing) nodes to visualize the structure.
    The printing stops when there are no more non-None nodes to process.
    """
    if not root:
        print("Tree is empty.")
        return

    # Initialize a deque (double-ended queue) for efficient adding/removing from both ends.
    # It will store nodes to be processed at the current level.
    queue = deque([root])

    # Continue as long as there is at least one non-None node in the queue.
    # This ensures we don't print endless lines of 'N's for empty branches.
    while any(node is not None for node in queue):
        level_size = len(queue)  # Number of nodes at the current level
        current_level_values = []  # List to store string representations of node values for the current level

        for _ in range(level_size):
            node = queue.popleft()  # Get the node from the front of the queue (FIFO)

            if node:
                current_level_values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                current_level_values.append("N")
                queue.append(None)
                queue.append(None)

        print(" ".join(current_level_values))

def bfs_traversal(root):
    if not root:
        return root
    stack=[root]
    res=[]
    while stack:
        node = stack.pop(0)
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res
# Test
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root = create_binary_tree(nums)
print_tree_level_by_level(tree_root)
print(bfs_traversal(tree_root))
