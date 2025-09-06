class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
def create_sorted_dll_with_repetitions(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head
values = [1, 2, 2, 3, 3, 3, 4,5,7]
dll_head = create_sorted_dll_with_repetitions(values)

# Helper function to print the list forward
def print_dll(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "\n")
        current = current.next
print_dll(dll_head)

def removeduplicate(head):
    if not head or not head.next:
        return head

    current=head
    while current and current.next:
        if current.data==current.next.data:
            next_node=current.next.next
            current.next=next_node
            if next_node:
                next_node.prev=current
        else:
            current=current.next
    return  head





# Helper function to print the list forward
def print_dll(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "\n")
        current = current.next
print_dll(removeduplicate(dll_head))


def removeduplicate2(head):
    if not head or not head.next:
        return head

    current=head
    while current and current.next:
        next_node=current.next
        while next_node and current.data==next_node.data:
            next_node=next_node.next

        current.next=next_node
        if next_node:
            next_node.prev=current
        current=current.next
    return head
print_dll(removeduplicate2(dll_head))
