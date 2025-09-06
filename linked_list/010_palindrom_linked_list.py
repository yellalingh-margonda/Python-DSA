class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to print the linked list
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


# Function to check if the linked list is a palindrome
def isPalindrome(head):
    if not head:
        return True

    slow = head
    fast = head

    # Move slow to the middle of the list, and fast to the end
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # If the list has an odd length, slow is at the middle element, so move it to the second half
    if fast:  # Means odd length list, so we need to move `slow` one step forward
        slow = slow.next

    # Reverse the second half of the list
    second_half = reverse_linked(slow)
    first_half = head

    # Compare the two halves
    while second_half:  # Only need to compare the second half
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# Test with an example list of size 7 (1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

print("Original list:")
print_list(head)

print("Is palindrome?", isPalindrome(head))  # Output should be False

# Test with an example list of size 6 (1 -> 2 -> 3 -> 4 -> 5 -> 6)
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(3)
head2.next.next.next.next = Node(2)
head2.next.next.next.next.next = Node(1)

print("\nOriginal list:")
print_list(head2)

print("Is palindrome?", isPalindrome(head2))  # Output should be False
