
def minwindow(s,t):
    l,  n = 0,  len(s)
    t_map={}
    for i in range(len(t)):
        t_map[t[i]]=t_map.get(t[i],0)+1
    formed=0
    required = len(t_map)
    window_counts = {}  # Character frequency in the window
    min_size = float('inf')
    min_word = ""
    for r in range(n):
        char=s[r]
        window_counts[char]= window_counts.get(char,0)+1
        if char in t_map and window_counts[char]==t_map[char]:
            formed+=1
        while l<=r and formed==required:
            if r-l+1< min_size:
                min_size=r-l+1
                min_word=s[l:r+1]
            left_char=s[l]
            window_counts[left_char]-=1

            if left_char in t_map and window_counts[left_char]<t_map[left_char]:
                formed-=1
            l+=1
    return min_word

s = "ADOBECODEBANC"
t = "ABC"
print(minwindow(s,t))

