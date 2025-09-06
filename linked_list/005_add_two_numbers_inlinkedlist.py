class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    dummy=Node(0)
    carry=0
    n1=head1
    n2=head2
    cur=dummy
    while n1 or n2 or carry:
        num=(n1.data if n1 else 0)+(n2.data if n2 else 0)+carry
        carry=num//10
        digit =num%10
        cur.next=Node(digit)
        cur=cur.next
        n1=n1.next if n1 else None
        n2=n2.next if n2 else None
    return dummy.next
