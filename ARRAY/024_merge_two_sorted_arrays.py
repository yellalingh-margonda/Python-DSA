def merge(a,b):
    left,right=len(a)-1,0
    while left >= 0 and right < len(b):
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
            break

    return sorted(a)+sorted(b)

A=[1, 8, 8]
B=[2, 3, 4, 5]
print(merge(A,B))



