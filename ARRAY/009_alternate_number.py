from typing import *


def alternateNumbers(a: List[int]) -> List[int]:
    pos = []
    neg = []

    for num in a:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    res = []
    i = 0
    j = 0
    n = len(a)

    # Start with positive if positive is more, else negative
    turn_pos = True if len(pos) >= len(neg) else False

    while i < len(pos) and j < len(neg):
        if turn_pos:
            res.append(pos[i])
            i += 1
        else:
            res.append(neg[j])
            j += 1
        turn_pos = not turn_pos

    # Append remaining
    while i < len(pos):
        res.append(pos[i])
        i += 1

    while j < len(neg):
        res.append(neg[j])
        j += 1

    return res
