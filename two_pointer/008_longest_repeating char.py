def longest_strg(strs, k):
    l,n,maxi=0,len(strs),0
    hash_map={}
    max_freq=0
    for r in range(n):
        hash_map[strs[r]]=hash_map.get(strs[r],0)+1
        max_freq = max(max_freq, hash_map[strs[r]])
        length=r-l+1
        while length-max_freq>k:
            hash_map[strs[l]]-=1
            l+=1
            length = r - l + 1
        maxi=max(maxi, r-l+1)
    return maxi
s = "AABABBA"
k = 1
print(longest_strg(s,k))