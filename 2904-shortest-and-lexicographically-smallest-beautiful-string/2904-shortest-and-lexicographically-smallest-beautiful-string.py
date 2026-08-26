class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        valid = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j].count('1') == k]
        return min(valid, key=lambda x: (len(x), x), default="")