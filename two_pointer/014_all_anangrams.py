def find_anagram(s, p):
    n, k = len(s), len(p)
    if n < k:
        return []

    p_map = {}
    for char_p in p:
        p_map[char_p] = p_map.get(char_p, 0) + 1

    window_map = {}
    result = []

    # matched_chars keeps track of how many characters in the current window
    # match the required count in p_map.
    # When matched_chars == len(p_map), it means all distinct characters
    # from p are present in the window with correct frequencies.
    matched_chars = 0

    left = 0
    for right in range(n):
        char_right = s[right]
        window_map[char_right] = window_map.get(char_right, 0) + 1

        # If the current character is in p_map and its count in the window_map
        # matches its required count in p_map, increment matched_chars.
        if char_right in p_map and window_map[char_right] == p_map[char_right]:
            matched_chars += 1

        # Shrink the window from the left if it's larger than p
        if right - left + 1 > k:
            char_left = s[left]

            # If the character being removed from the left was a 'matched' character,
            # decrement matched_chars as its count will now be less than required.
            if char_left in p_map and window_map[char_left] == p_map[char_left]:
                matched_chars -= 1

            window_map[char_left] -= 1
            if window_map[char_left] == 0:
                del window_map[char_left]
            left += 1

        # Check for anagram
        # Anagram found if the window size is k and all characters are matched
        if right - left + 1 == k and matched_chars == len(p_map):
            result.append(left)

    return result