class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def helper(node):
    if not node:
        return 1
    carry_from_right = helper(node.next)
    sum_val = node.data + carry_from_right
    node.data = sum_val % 10
    return sum_val // 10
def addOne(head: Node) -> Node:
    final_carry = helper(head)
    if final_carry > 0:
        new_head = Node(final_carry) # Create a new node with the remaining carry
        new_head.next = head         # Point this new node to the original head
        return new_head              # The new node becomes the head of the list
    else:
        # If no final carry, the original head (possibly with updated data) is the result.
        return head

# Helper function to print the linked list (for testing)
def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Test cases
# 99 + 1 = 100
head_99 = Node(9, Node(9))
print("Original list (99):")
print_list(head_99)
result_99 = addOne(head_99)
print("Result (99 + 1):")
print_list(result_99) # Expected: 1 -> 0 -> 0 -> None

# 123 + 1 = 124
head_123 = Node(1, Node(2, Node(3)))
print("\nOriginal list (123):")
print_list(head_123)
result_123 = addOne(head_123)
print("Result (123 + 1):")
print_list(result_123) # Expected: 1 -> 2 -> 4 -> None

# 0 + 1 = 1
head_0 = Node(0)
print("\nOriginal list (0):")
print_list(head_0)
result_0 = addOne(head_0)
print("Result (0 + 1):")
print_list(result_0) # Expected: 1 -> None

# 9 + 1 = 10
head_9 = Node(9)
print("\nOriginal list (9):")
print_list(head_9)
result_9 = addOne(head_9)
print("Result (9 + 1):")
print_list(result_9) # Expected: 1 -> 0 -> None