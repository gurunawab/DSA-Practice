class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for c1 in text1:
            prev = 0
            for j, c2 in enumerate(text2):
                prev, dp[j + 1] = dp[j + 1], prev + 1 if c1 == c2 else max(dp[j + 1], dp[j])
        return dp[-1]