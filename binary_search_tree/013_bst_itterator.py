class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    # Helper to push all left nodes to the stack
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        # Top of stack is the next smallest element
        node = self.stack.pop()
        val = node.val

        # If the node has a right child, process its leftmost path
        if node.right:
            self._leftmost_inorder(node.right)

        return val

    def hasNext(self):
        return len(self.stack) > 0
