class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next=odd.next.next
            odd= odd.next
            even.next = even.next.next
            even = even.next
        odd.next=even_head

        return  head