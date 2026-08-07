class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c**0.5)
        while a <= b:
            s = a * a + b * b
            if s == c: return True
            a, b = (a + 1, b) if s < c else (a, b - 1)
        return False