def substring_count_brut(s):
    count, n = 0, len(s)

    for i in range(n):
        hash_map = {}
        for j in range(i, n):
            hash_map[s[j]] = 1  # or any value
            if len(hash_map) == 3:
                count += 1
            elif len(hash_map) > 3:
                break

    return count


def substring_count_brut_opt(strs):
    count,n=0, len(strs)
    for i in range(n):
        hash_map={}
        for j in range(i, n):
            hash_map[strs[j]] = hash_map.get(strs[j],1)
            if len(hash_map) == 3:
                count += n-j
                break
    return count


def substring_count_optimal(strs):
    l,count,n=0,0, len(strs)
    hash_map = {}
    for r in range(n):
        hash_map[strs[r]] = r
        if len(hash_map)<3:
            continue
        count+=min(hash_map.values())+1
    return  count

print(substring_count_optimal('bbacba'))
