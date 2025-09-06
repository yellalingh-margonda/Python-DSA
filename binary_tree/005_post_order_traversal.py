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


def post_order_itterative(root):
    if not root:
        return []
    stack1=[root]
    stack2=[]
    while stack1:
        node=stack1.pop()
        stack2.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return stack2[::-1]
print(post_order_itterative(tree_root))
def post_order(root, res=None):
    if res is None:
        res = []
    if root:
        post_order(root.left, res)
        post_order(root.right, res)
        res.append(root.val)

    return res
print(post_order(tree_root))

