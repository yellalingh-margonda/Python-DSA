class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(node,val):
    if not node:
        return Node(val)
    if val<node.val:
        node.left=insert_node(node.left,val)
    else:
        node.right = insert_node(node.right, val)
    return node

def create_binary_tree(nums):
    if not nums:
        return None

    root = Node(nums[0])
    for ele in nums[1:]:
        insert_node(root, ele)
    return root

nums = [10, 5, 15, 2, 7, 12, 20]
tree_root =  create_binary_tree(nums)

def in_order(root):
    stack=[]
    node=root
    res=[]
    while True:
        if node:
            stack.append(node)
            node=node.left
        else:
            if not stack:
                break
            current = stack.pop()  # Get the full node, not just the value
            res.append(current.val)
            node = current.right
    return  res


