def permutations(s1,s2):
    if len(s2)>len(s1):
        return False
    l,n=0, len(s1)
    s2_map={}
    for ele in s2:
        s2_map[ele]=s2_map.get(ele,0)+1
    s1_map={}
    formed=0
    required=len(s2_map)
    k=len(s2)
    for r in range(n):
        char=s1[r]
        s1_map[char]=s1_map.get(char,0)+1
        if char in s2_map and s1_map[char]==s2_map[char]:
            formed+=1

        if r-l+1>k:
            left_char=s1[l]
            if left_char in s2_map and s1_map[left_char] == s2_map[left_char]:
                formed -= 1
            s1_map[left_char] -= 1
            if s1_map[left_char] == 0:
                del s1_map[left_char]
            l+=1
        if formed==required and r-l+1==k:
            return True
    return False

print(permutations("oidbcaf", "abc"))  # True (substring "bca")
print(permutations("odicf", "dc"))     # False
print(permutations("bcdxabcdy", "bcdyabcdx"))  # True
