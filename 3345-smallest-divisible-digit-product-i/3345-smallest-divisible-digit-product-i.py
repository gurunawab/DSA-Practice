class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return next(x for x in count(n) if eval('*'.join(str(x))) % t == 0) 