class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def find_tail(head):
    current= head
    while current.next:
        current=current.next
    return current

def findPairs(head: Node, k: int) -> [[int]]:
    tail=find_tail(head)
    left, right=head,tail
    res=[]
    while left and right and left != right and left.prev != right:
        total= left.data+right.data
        if total==k:
            res.append([left.data, right.data])
            left= left.next
            right=right.prev
        elif total>k:
            right=right.prev
        else:
            left=left.next

    return res