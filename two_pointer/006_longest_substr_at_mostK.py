def kDistinctChars(k, str):
    l, maxi,n=0,0, len(str)
    frequency_map={}
    for r in range(n):
        frequency_map[str[r]]=frequency_map.get(str[r],0)+1
        while len(frequency_map)>k:
            frequency_map[str[l]]-=1
            if frequency_map[str[l]]==0:
                del frequency_map[str[l]]
            l+=1
        maxi=max(maxi, r-l+1)
    return maxi

