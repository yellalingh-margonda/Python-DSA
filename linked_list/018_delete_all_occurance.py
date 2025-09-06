class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    temp=head

    while temp:
        if temp.data==k:
            if temp==head:
                head=head.next
            next_node=temp.next
            prev_node=temp.prev
            if next_node:
                next_node.prev=prev_node
            if prev_node:
                prev_node.next=next_node
            temp = temp.next if temp.next else None
        else:
            temp=temp.next
    return head