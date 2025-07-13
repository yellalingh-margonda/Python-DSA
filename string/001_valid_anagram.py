class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Count the frequencies of characters in both strings
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Compare the two frequency dictionaries
        return freq_s == freq_t
