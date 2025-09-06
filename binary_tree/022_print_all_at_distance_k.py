# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def pre_order(node, parent_map):
    if not node:
        return parent_map
    if node.left:
        parent_map[node.left]=node
        pre_order(node.left, parent_map)
    if node.right:
        parent_map[node.right]=node
        pre_order(node.right, parent_map)
    return parent_map

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        visited = set()
        queue = [target]
        parent_map = pre_order(root, {})
        distance = 0

        while queue:
            if distance == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.pop(0)
                visited.add(node)

                # Add left child
                if node.left and node.left not in visited:
                    queue.append(node.left)

                # Add right child
                if node.right and node.right not in visited:
                    queue.append(node.right)

                # Add parent
                if node in parent_map and parent_map[node] not in visited:
                    queue.append(parent_map[node])

            distance += 1

        return []