prev=None

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #     1
    #    / \
    #   2   5
    #  / \    \
    # 3   4    6
    #        /
    #       7

# During the execution of the `flatten()` function, the traversal processes
# the nodes in reverse preorder (right → left → root), allowing us to reconstruct
# the tree as a singly linked list in-place using the `right` pointers. Initially,
# `prev` is set to `None`. When the recursion reaches node `7`, it processes its right
# and left subtrees (both `None`) and sets `7.right = prev` (which is `None`) and
# `7.left = None`, then updates `prev` to node `7`. Returning to node `6`, its right
# subtree (node `7`) has already been processed, and its left is `None`. It then sets
# `6.right = prev` (now pointing to node `7`) and `6.left = None`, and updates `prev`
# to node `6`. This process ensures that each node points to the previously processed
# node via its `right` pointer, gradually flattening the entire tree into a right-skewed
# linked list following preorder traversal.

def flatten(node):
    global prev
    if not node:
        return
    flatten(node.right)
    flatten(node.left)
    node.right=prev
    node.left=None
    prev=node
    return
def print_flattened(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

# Build the tree
root = Node(1)
root.left = Node(2, Node(3), Node(4))
root.right = Node(5, None, Node(6))

flatten(root)
print_flattened(root)
