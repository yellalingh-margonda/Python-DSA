class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def create_linked_list(nums):
    if not nums:
        return None
    head = Node(nums[0])
    current = head
    for val in nums[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
    return head
def print_linkedList(head):
    current=head
    while current:
        print(current.data,end="->" if current.next else "\n")
        current=current.next
    return


def find_mid(head):
    slow,fast=head,head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow

head= create_linked_list([7,2,1,6,3,9,5])
print_linkedList(head)

def merge(head1, head2):
    if not head1 or not head2:
        return head1 if head1 else head2
    dummy_node = Node(-1)
    current = dummy_node
    t1 = head1
    t2 = head2
    while t1 and t2:
        if t1.data < t2.data:  # fix: compare with t2.data, not t2
            current.next = t1
            t1 = t1.next
        else:
            current.next = t2
            t2 = t2.next
        current = current.next
    if t1:
        current.next = t1
    if t2:
        current.next = t2
    return dummy_node.next
def sort_linkedlist(head):
    if not head or not head.next:
        return head
    mid = find_mid(head)
    right_head = mid.next
    left_head = head
    mid.next = None
    left_list = sort_linkedlist(left_head)
    right_list = sort_linkedlist(right_head)
    return merge(left_list, right_list)

print_linkedList(sort_linkedlist(head))

