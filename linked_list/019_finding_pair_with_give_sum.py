class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def findPairs(head: Node, k: int) -> [[int]]:
    res = []
    temp1 = head

    while temp1:
        temp2 = temp1.next
        while temp2:
            # Check if the pair sums to k
            if temp1.data + temp2.data == k:
                res.append([temp1.data, temp2.data])
            if temp1.data + temp2.data > k:
                break
            temp2 = temp2.next  # Move temp2 to the next node
        temp1 = temp1.next  # Move temp1 to the next node

    return res

