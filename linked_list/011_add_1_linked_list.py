class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_linked_list_iterative(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def addOne(head: Node) -> Node:
    if not head:
        return Node(1)  # If list is empty, return a node with 1

    # Step 1: Reverse the list
    head = reverse_linked_list_iterative(head)

    # Step 2: Add one
    current = head
    carry = 1
    prev = None
    while current:
        sum_val = current.data + carry
        current.data = sum_val % 10
        carry = sum_val // 10
        prev = current
        current = current.next

    # Step 3: If carry still remains, add a new node
    if carry:
        prev.next = Node(carry)

    # Step 4: Reverse the list again
    head = reverse_linked_list_iterative(head)
    return head
