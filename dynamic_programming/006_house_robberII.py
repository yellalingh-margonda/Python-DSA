def house_robber2(n, array):
    if n==0:
        return array[n]
    if n<0:
        return 0
    left =array[n]+house_robber2(n-2, array)
    right=house_robber2(n-1,array)
    return max(left,right)

