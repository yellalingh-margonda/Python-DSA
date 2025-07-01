def frog_jump(array,n,l):
    if n==array[-1]:
        return True
    for i in [l-1,l, l+1]:
        if i>0:
            if n+i in array:
               if frog_jump(array,n+i,i):
                   return True
    return False


def frog_jump(array, n, l, dp=None):
    max_jump = len(array)  # To limit dp array size
    pos_to_index = {pos: i for i, pos in enumerate(array)}  # position → index mapping

    if dp is None:
        dp = [[-1] * (max_jump + 1) for _ in range(len(array))]

    if n == array[-1]:
        return True

    idx = pos_to_index[n]
    if dp[idx][l] != -1:
        return dp[idx][l] == 1

    for i in [l - 1, l, l + 1]:
        if i > 0:
            next_pos = n + i
            if next_pos in pos_to_index:
                if frog_jump(array, next_pos, i, dp):
                    dp[idx][l] = 1
                    return True

    dp[idx][l] = 0
    return False
