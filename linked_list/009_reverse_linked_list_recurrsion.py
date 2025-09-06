class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(node):
    if not node or not node.next:
        return node  # Return the last node (this is the new head)

    new_head = reverse_linked_list(node.next)  # Recursively reverse the rest of the list

    # Reverse the current node
    node.next.next = node
    node.next = None  # Set the current node's next to None, as it's now the last node

    return new_head  # Return the new head of the reversed list


def print_list(node):
    while node:
        print(node.data, end=" -> " if node.next else " -> None")
        node = node.next
    print()

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed list:")
print_list(reversed_head)
