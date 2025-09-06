#one of the most important take aways is we are checing current.next so current should not ne none and current.next.next this impliese current.next should not be none
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        arr=[]
        current=head
        while  current and current.next:
            arr.append(current.val)
            current=current.next.next
        if current:
            arr.append(current.val)
        current=head.next
        while  current and current.next:
            arr.append(current.val)
            current=current.next.next
        if current:
            arr.append(current.val)
        i=0
        current=head
        while current:
            current.val=arr[i]
            i+=1
            current=current.next
        return head