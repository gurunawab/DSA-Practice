class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n:
            if (n & 3) == 3:
                n += 1
                ans += 1
            else:
                ans += n & 1
                n >>= 1
        return ans