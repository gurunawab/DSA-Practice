class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2
        val = lambda c: 4.5 if c == '?' else int(c)
        return sum(map(val, num[:mid])) != sum(map(val, num[mid:]))