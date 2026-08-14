class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i = 0
        for j in range(len(s)):
            i += any(s[i:j+1].count(c) > 2 for c in s[i:j+1])
        return len(s) - i