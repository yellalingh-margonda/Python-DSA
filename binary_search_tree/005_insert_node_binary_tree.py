class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Insert function for BST
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
values = [10, 5, 15, 3, 7, 12, 18]
root = None
for v in values:
    root = insert(root, v)


def insert_node(root, val):
    if not root:
        return  Node(val)
    cur=root

    while True:
        if cur.val <=val:
            if  cur.right:
                cur=cur.right
            else:
                cur.right =Node(val)
                break
        else:
            if cur.left:
                cur=cur.left
            else:
                cur.left=Node(val)
                break
    return root
