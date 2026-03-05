#Longest Substring with K uniques
def longestkSubstr(self, s, k):
    char_map = {}
    i = 0
    max_len = -1

    for j in range(len(s)):
        char_map[s[j]] = char_map.get(s[j], 0) + 1

        while len(char_map) > k:
            char_map[s[j]] -= 1
            if char_map[s[i]] == 0:
                del char_map[s[i]]
            i += 1

        if len(char_map) == k:
            max_len = max(max_len, j - i + 1)

    return max_len                