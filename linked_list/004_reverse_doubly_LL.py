'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

'''


def reverseDLL(head):
    stack = []
    temp = head

    # Push all node data into the stack
    while temp:
        stack.append(temp.data)
        temp = temp.next

    # Pop from stack and overwrite node data
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next

    return head


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

'''


def reverseDLL(head):
    current = head
    new_head = None
    last = None
    while current:
        last = current.prev
        current.prev = current.next
        current.next = last
        new_head = current
        current = current.prev
    return new_head