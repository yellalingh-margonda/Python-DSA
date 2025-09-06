# Intuition:
# Think of two pointers, slow and fast, moving through the linked list. Slow moves one step at a time, and fast moves two steps.
# If there's a cycle, the fast pointer will eventually "lap" the slow pointer inside the cycle — meaning they will meet.
# Once a cycle is detected (slow == fast), we reset a new pointer to the head. Now, both this new pointer and the slow pointer
# move one step at a time. They are guaranteed to meet at the start of the cycle. This works because of the math behind how far
# each pointer has traveled and the nature of the loop. If no cycle exists, the fast pointer will reach the end (None), and we return None.

# This is the clever part.
#
# At the Meeting Point:
#
# The slow pointer has traveled F+k steps.
#
# The fast pointer has traveled F+k+m⋅C steps (where m is some integer representing how many additional full cycles fast has completed within the loop before meeting slow).
#
# Since fast travels twice as fast as slow:
# 2⋅(F+k)=F+k+m⋅C
# 2F+2k=F+k+m⋅C
# F+k=m⋅C
#
# This equation is the heart of the algorithm. It means that the distance from the head to the meeting point (F + k) is a multiple of the cycle length.
# #
# We know that F+k=m⋅C.
# Rearranging this, we get F=m⋅C−k.
# This means if slow travels another F steps from its current position (the meeting point), it will land on the start of the cycle.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow=head
        fast=head
        index=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                pointer=head
                while pointer!=slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer
        return None