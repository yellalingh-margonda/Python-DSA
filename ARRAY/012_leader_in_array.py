def findLeaders(elements, n):
    maxi= float('-inf')
    leaders=[]
    for i in range(n-1,-1,-1):
        if elements[i]>maxi:
            maxi=elements[i]
            leaders.append(elements[i])
    leaders.reverse()
    return leaders


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxi = -1

        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxi
            maxi = max(maxi, curr)

        return arr
