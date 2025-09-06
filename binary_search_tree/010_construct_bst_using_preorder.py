class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_from_preorder(preorder):
    def build(bound=float('inf')):
        nonlocal idx
        if idx == len(preorder) or preorder[idx] > bound:
            return None

        root = Node(preorder[idx])
        idx += 1
        root.left = build(root.val)
        root.right = build(bound)
        return root   

    idx = 0
    return build()
