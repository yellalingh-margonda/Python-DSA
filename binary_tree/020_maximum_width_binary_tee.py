from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_length = len(queue)

            # Get the index of the first node in the current level
            _, first_index = queue[0]
            _, last_index = queue[-1]

            # Calculate the width of the current level
            current_width = last_index - first_index + 1

            # Update the maximum width
            max_width = max(max_width, current_width)

            for _ in range(level_length):
                node, index = queue.popleft()

                # Add left child to the queue with its correct index
                if node.left:
                    queue.append((node.left, 2 * index + 1))

                # Add right child to the queue with its correct index
                if node.right:
                    queue.append((node.right, 2 * index + 2))

            # Get the index of the last node in the current level

        return max_width