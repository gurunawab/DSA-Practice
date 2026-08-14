class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        for c1 in word1:
            prev, dp[0] = dp[0], dp[0] + 1
            for j, c2 in enumerate(word2):
                prev, dp[j + 1] = dp[j + 1], prev if c1 == c2 else 1 + min(prev, dp[j], dp[j + 1])
        return dp[-1]