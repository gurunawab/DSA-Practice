class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(-d[a] if d[a] < d[b] else d[a] for a, b in zip(s, s[1:])) + d[s[-1]]