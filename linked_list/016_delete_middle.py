class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMiddle(head):
    if not head or not head.next:
        return Node(-1)
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    delete = count // 2 - 1
    current = head
    while current:
        if delete == 0:
            current.next = current.next.next
            return head
        current = current.next
        delete -= 1
    return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteMiddle(head):
    if not head or not head.next:
        return Node(-1)
    slow = head
    fast = head
    i = 0
    while fast and fast.next:
        if i > 0:
            slow = slow.next

        fast = fast.next.next
        i += 1
        if slow == fast:
            break
    slow.next = slow.next.next
    return head