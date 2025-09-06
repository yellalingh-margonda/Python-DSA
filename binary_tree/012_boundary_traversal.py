left_res=[]
def left_boundary(node):
    if not node or (not node.left and not node.right):
        return
    left_res.append(node.val)
    if node.left:
        left_boundary(node.left)
    elif node.right:
        left_boundary(node.right)
    return
bottom_res=[]
def bottom_boundary(node):
    if not node:
        return
    if not node.left and not node.right:
        bottom_res.append(node.val)
    bottom_boundary(node.left)
    bottom_boundary(node.right)
    return
right_res=[]
def right_boundary(node):
    if not node or (not node.left and not node.right):
        return
    right_res.append(node.val)
    if node.right:
        right_boundary(node.right)
    elif node.left:
        right_boundary(node.left)
    return

def boundary_traversal(root):
    if not root:
        return []
    if root.left:
        left_boundary(root.left)
    bottom_boundary(root)
    if root.right:
        right_boundary(root.right)
    return [root.val]+left_res+bottom_res+right_res[::-1]
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


nums=[20, 8, 22, 4, 12, 25, None, None, None, 10, 14]
root=build_tree(nums)
print(boundary_traversal(root))