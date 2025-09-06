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
nums=[1,4,5,8,9]
head1=create_linked_list(nums)
nums=[2,3,6,7,10]
head2=create_linked_list(nums)
def print_linkedList(head):
    current=head
    while current:
        print(current.data,end="->" if current.next else "\n")
        current=current.next
    return
def merge_sorted_linked_list(head1,head2):
    if  not head1 or not head2:
        return  head1 if head1 else head2
    dummy_node=Node(-1)
    current= dummy_node
    first, second =head1, head2
    while first and second:
        if first.data<=second.data:
            current.next=first
            first=first.next
        else:
            current.next = second
            second = second.next
        current=current.next
    if first:
        current.next=first
    if second:
        current.next=second
    return dummy_node.next

head=merge_sorted_linked_list(head1,head2)

print_linkedList(head)

