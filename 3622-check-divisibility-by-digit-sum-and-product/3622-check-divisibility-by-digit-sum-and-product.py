import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        return n % (sum(digits) + math.prod(digits)) == 0