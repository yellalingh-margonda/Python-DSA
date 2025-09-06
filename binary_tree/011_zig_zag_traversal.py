class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None
    from collections import deque

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def zig_zag_traversal(root):
    if not root:
        return []

    flag = True
    stack = [root]
    res = []

    while stack:
        level_size = len(stack)
        level_vals = []
        level_stack = []

        for i in range(level_size):
            if flag:
                node = stack.pop(0)
                level_vals.append(node.val)
                if node.left:
                    level_stack.append(node.left)
                if node.right:
                    level_stack.append(node.right)
            else:
                node = stack.pop(-1)
                level_vals.append(node.val)
                if node.right:
                    level_stack.insert(0, node.right)
                if node.left:
                    level_stack.insert(0, node.left)

        res.append(level_vals)
        stack = level_stack
        flag = not flag

    return res

# Test
tree = build_tree([3, 9, 20, None, None, 15, 7])
print(zig_zag_traversal(tree))  # Expected: [[3], [20, 9], [15, 7]]
