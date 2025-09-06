class Node:
     def __init__(self, data, next=None):
         self.data=data
         self.next=next


def create_linked_list(nums):
    if not nums:
        return None
    head=Node(nums[0])
    current=head
    for val in nums[1:]:
        new_node=Node(val)
        current.next=new_node
        current=new_node
    return head
def print_linkedList(head):
    current=head
    while current:
        print(current.data,end="->" if current.next else "\n")
        current=current.next
    return
nums=[1,2,3,4,5,6,7]
head=create_linked_list(nums)
print_linkedList(head)

def rotate_linkedlist(head,k):
    count=0
    current=head
    while current:
        count+=1
        tail=current
        current=current.next
    k=k%count
    if k==0 or k==count:
        return head
    tail.next=head
    current=head
    for _ in range(count-k-1):
        current=current.next
    head=current.next
    current.next=None
    return head

head=rotate_linkedlist(head,2)
print_linkedList(head)