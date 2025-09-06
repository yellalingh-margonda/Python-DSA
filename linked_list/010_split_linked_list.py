class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print linked list
def print_list(node):
    while node:
        print(node.data, end=" -> " if node.next else " -> None")
        node = node.next
    print()

# Function to reverse a linked list
def reverse_linked(node):
    prev = None
    current = node
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to find the middle of the list and split it into two halves
def split_list(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # Split into two halves
    first_half = head
    second_half = slow.next
    slow.next = None  # Disconnect the first half from the second half
    return first_half, second_half

# Create a linked list for testing (size 7: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

# # Split the list into two halves
# first_half, second_half = split_list(head)
#
# # Reverse the second half
# reversed_second_half = reverse_linked(second_half)
#
# # Print the first half and reversed second half
# # print("First half:")
# # print_list(first_half)
# #
# # print("Reversed second half:")
# # print_list(reversed_second_half)


# Create a linked list for testing (size 7: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(1)

# Split the list into two halves
first_half, second_half = split_list(head)

# Reverse the second half
reversed_second_half = reverse_linked(second_half)

# Print the first half and reversed second half
print("First half:")
print_list(first_half)

print("Reversed second half:")
print_list(reversed_second_half)

