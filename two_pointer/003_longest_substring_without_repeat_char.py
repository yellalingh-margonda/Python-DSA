def substring(strs):
    i, n=0, len(strs)
    maxi=0
    for i in range(n):
        hash_set=set()
        for j in range(i,n):
             if strs[j] in hash_set:
                 break
             hash_set.add(input[j])
             maxi=max(maxi,j-i+1)
    return  maxi

# Absolutely — using **“right pointer”** instead of **“last occurrence”** makes it clearer and ties better with the sliding window logic.
#
# Here’s the **final refined summary**:
#
# This function computes the length of the longest substring without repeating
# characters using a sliding window and a hash map. As the right pointer moves through the string,
# it checks if the current character has appeared before within the current window.
# If so, the left pointer jumps directly to one position after the previous index of that character
# (tracked in the hash map), ensuring all characters in the window remain unique.
# This jump skips intermediate windows which, although valid, would be smaller than the current
# one and therefore not useful for the result. The function updates the maximum window length
# at each step and returns the longest found.

def substring_optimal(strs):
    l,r,=0,0
    hash_map={}
    n=len(strs)
    maxi = 0
    while r<n:
        if strs[r] in hash_map and hash_map[strs[r]] >= l:
            l= hash_map[strs[r]]+1
        hash_map[strs[r]]=r
        maxi=max(maxi,r-l+1)
        r+=1
    return  maxi

print(substring_optimal("abcabcbb"))  # Output: 3
print(substring_optimal("bbbbb"))     # Output: 1
print(substring_optimal("pwwkew"))    # Output: 3
