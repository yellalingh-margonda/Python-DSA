class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Serialization
def serialize(root):
    if not root:
        return []

    queue = [root]
    res = []

    while queue:
        node = queue.pop(0)  # Dequeue node
        if node:
            res.append(node.val)
            queue.append(node.left)  # Enqueue left child
            queue.append(node.right)  # Enqueue right child
        else:
            res.append('#')  # Mark null nodes with '#'
    return res


# Deserialization
def deserialize(data):
    if not data:
        return None

    root_val = data.pop(0)
    if root_val == '#':
        return None

    root = Node(root_val)
    queue = [root]

    while queue and data:
        parent = queue.pop(0)

        # Left child
        left_val = data.pop(0)
        if left_val != '#':
            left=Node(left_val)
            parent.left = left
            queue.append(left)

        # Right child
        right_val = data.pop(0)
        if right_val != '#':
            right=Node(right_val)
            parent.right = right
            queue.append(right)

    return root


# Function to print the tree (for verification)
def print_tree(root):
    if not root:
        return []
    return [root.val] + print_tree(root.left) + print_tree(root.right)


# Example Usage
# Constructing a binary tree:
#         1
#        / \
#       2   3
#      / \   / \
#     4   5 6   7

root = Node(1)
root.left = Node(2,  Node(5))
root.right = Node(3, Node(6), Node(7))

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
print(inorder(root))
# Serialize the tree
serialized_data = serialize(root)
print(f"Serialized: {serialized_data}")

# Deserialize the data back to the tree
deserialized_root = deserialize(serialized_data)
print(f"Deserialized Preorder: {print_tree(deserialized_root)}")
print(inorder(root))