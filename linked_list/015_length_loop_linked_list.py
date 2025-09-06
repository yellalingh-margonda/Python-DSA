class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    map={}
    current=head
    i=0
    while current:
        if current in map:
            return i-map[current]
        map[current]=i
        i+=1
        current=current.next
    return 0
