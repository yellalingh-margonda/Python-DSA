'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def sortList(head):
    if not head:
        return head
    count_0 = 0
    count_1 = 0
    count_2 = 0
    temp = head
    while temp:
        if temp.data == 0:
            count_0 += 1
        elif temp.data == 1:
            count_1 += 1
        else:
            count_2 += 1
        temp = temp.next
    temp = head
    while count_0 > 0:
        temp.data = 0
        temp = temp.next
        count_0 -= 1
    while count_1 > 0:
        temp.data = 1
        temp = temp.next
        count_1 -= 1
    while count_2 > 0:
        temp.data = 2
        temp = temp.next
        count_2 -= 1
    return head
class Node:
     def __init__(self, data, next=None):
         self.data=data
         self.next=next

def sortList(head):
    if not head:
        return  head

    zerohead = Node(-1)
    onehead = Node(-1)
    twohead = Node(-1)
    zero = zerohead
    one = onehead
    two =twohead
    current=head
    while current:
        if current.data==0:
            zero.next=current
            zero=current
        elif current.data==1:
            one.next=current
            one=current
        else:
            two.next = current
            two = current
        current=current.next
    zero.next= onehead.next if onehead.next else twohead.next
    one.next = twohead.next
    two.next = None
    return zerohead.next

