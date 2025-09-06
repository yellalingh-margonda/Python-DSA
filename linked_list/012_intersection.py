'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def findIntersection(firstHead, secondHead):
    memo = {}
    i = 0
    current = firstHead
    while current:
        memo[current] = 1
        i += 1
        current = current.next
    current = secondHead
    while current:
        if current in memo:
            return current
        current = current.next
    return None


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
# Imagine two runners, Alice and Bob, starting on two different tracks
# (linked lists) that may merge at some point. They run at the same speed,
# and when they reach the end of their track, they switch to the start of the other’s track.
# If the tracks intersect, the runners will meet at the intersection node after covering equal total distances. If there's no intersection, they'll both reach the end (None) at the same time without meeting. This logic ensures detection of the intersection point without using extra space.


def findIntersection(firstHead, secondHead):
    pointer1, pointer2=firstHead,secondHead

    while pointer1 != pointer2:
        pointer1= pointer1.next if pointer1 else pointer2
        pointer2= pointer2.next if pointer2 else pointer2

    return pointer2