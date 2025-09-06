class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def create_sorted_ll_with_repetitions(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return head


def print_ll(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "\n")
        current = current.next


# This is the correct recursive reversal for a SINGLY-LINKED LIST.
def revese_ll_singly(node):
    if not node or not node.next:
        return node
    new_head = revese_ll_singly(node.next)
    node.next.next = node
    node.next = None
    return new_head


# A helper function to find the kth node from a given node.
def find_kth_node(node, k):
    current = node
    for _ in range(k - 1):
        if not current:
            return None
        current = current.next
    return current


# The main function to reverse groups of k nodes.
# It uses the recursive singly-linked list reversal as a subroutine.
def reverse_kgroup(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev_tail = dummy

    current = head

    while current:
        kth_node = find_kth_node(current, k)

        # If there are not enough nodes left, link the last tail to the rest
        # and we are done.
        if not kth_node:
            prev_tail.next = current
            break

        # Store the head of the next group
        next_group_head = kth_node.next

        # Temporarily detach the current k-group
        kth_node.next = None

        # Reverse the current k-group using the singly-linked list reversal
        reversed_head = revese_ll_singly(current)

        # Connect the previous group's tail to the new head of the reversed group
        prev_tail.next = reversed_head

        # The original 'current' is now the new tail of the reversed group
        new_tail = current

        # Update the prev_tail for the next iteration
        prev_tail = new_tail

        # Connect the new tail of the reversed group to the next group
        new_tail.next = next_group_head

        # Move to the next group
        current = next_group_head

    return dummy.next


# --- Execution ---
values = [1, 2, 2, 3, 3, 3, 4, 5, 7]
ll_head = create_sorted_ll_with_repetitions(values)

print("Original List:")
print_ll(ll_head)

k = 3
ll_head = reverse_kgroup(ll_head, k)

print(f"\nList after reversing every {k} nodes:")
print_ll(ll_head)