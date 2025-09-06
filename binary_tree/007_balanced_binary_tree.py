def balanced_tree(node):
    if not node:
        return 0
    left=balanced_tree(node.left)
    right=balanced_tree(node.right)
    if left==-1 or right==-1:
        return -1
    if abs(left-right)>1:
        return -1
    return 1+max(left,right)

class Solution:
    def isBalanced(self, root) -> bool:
        return False if balanced_tree(root)==-1 else True