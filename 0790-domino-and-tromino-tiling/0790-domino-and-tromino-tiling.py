class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c = 1, 1, 2
        for _ in range(n):
            a, b, c = b, c, (2 * c + a) % 1000000007
        return a