#in means root will be in between
#pre means root will be first
#post means root will be last
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

def print_tree(root):
    if not root:
        print('no data ')
        return
    stack=[root]

    while stack:
        stc_len=len(stack)
        current_level=[]
        for _ in range(stc_len):
            node=stack.pop(0)
            if node:
                current_level.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        print("->".join(current_level))
    return
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root =  create_binary_tree(nums)
print_tree(tree_root)

def pre_order(root, res=None):
    if res is None:
        res = []

    if root:
        res.append(root.val)
        pre_order(root.left, res)
        pre_order(root.right, res)

    return res
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root = create_binary_tree(nums)

def post_order(root, res=None):
    if res is None:
        res = []

    if root:

        post_order(root.left, res)
        post_order(root.right, res)
        res.append(root.val)

    return res
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root = create_binary_tree(nums)

print("Post-order Traversal:", post_order(tree_root))


def in_order(root, res=None):
    if res is None:
        res = []

    if root:
        in_order(root.left, res)
        res.append(root.val)
        in_order(root.right, res)
    return res
nums = [10, 5, 15, 2, 7, 12, 20]
tree_root = create_binary_tree(nums)

print("in-order Traversal:", in_order(tree_root))


def in_order2(root):
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)

print("in-order Traversal:", in_order2(tree_root))

def in_order3(root):
    if root is None:
        return []

    # Recursively get in-order traversal from left and right subtrees
    left = in_order(root.left)
    right = in_order(root.right)

    # Create a new list at this level and concatenate the results
    result = left + [root.val] + right
    return result
print("in-order Traversal:", in_order3(tree_root))