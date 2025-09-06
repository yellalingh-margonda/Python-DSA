# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head and not head.next:
            return head
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        index=count-n #5-2=3
        if index == 0:
            return head.next
        current= head
        i=0
        while i< index-1: #i<=2  when i is 1 then condtion holds good that as we are moving the current, when i is 1 then current points to 2
            current=current.next
            i+=1
        if current.next:
            current.next=current.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        if not head.next and n == 1:
            return None
        slow=head
        fast=head
        while n>0:
            fast=fast.next
            n-=1
        # If fast is None now, we're deleting the head
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head

