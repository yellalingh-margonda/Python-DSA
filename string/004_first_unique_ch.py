def firstUniqChar(s: str) -> int:
        freq_map = {}

        # Step 1: Build frequency map
        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        # Step 2: Find first character with frequency 1
        for i in range(len(s)):
            if freq_map[s[i]] == 1:
                return i

        return -1
