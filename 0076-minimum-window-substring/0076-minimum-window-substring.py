from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i = l = r = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not r or j - i < r - l:
                    l, r = i, j
        return s[l:r]