class Solution:

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last = {}

        for char in s:
           
            last[char] = (sum(last.values()) + 1) % MOD

        return sum(last.values()) % MOD