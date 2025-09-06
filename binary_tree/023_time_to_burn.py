# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from collections import deque


def pre_order(node, parent_map):
    if not node:
        return parent_map
    if node.left:
        parent_map[node.left] = node
        pre_order(node.left, parent_map)
    if node.right:
        parent_map[node.right] = node
        pre_order(node.right, parent_map)
    return parent_map


class Solution:
    def amountOfTime(self, root, start):
        parent_map = pre_order(root, {})

        # Find the node with the start value
        def find_start_node(node):
            if not node:
                return None
            if node.val == start:
                return node
            left = find_start_node(node.left)
            if left:
                return left
            return find_start_node(node.right)

            start_node = find_start_node(root)

            visited = set()
            queue = deque()
            queue.append(start_node)
            visited.add(start_node)

            distance = -1  # Adjust for overcounting last level
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    for neighbor in (node.left, node.right, parent_map.get(node)):
                        if neighbor and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                distance += 1

            return distance