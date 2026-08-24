class Solution:

    def stoneGameVIII(self, stones: List[int]) -> int:
        pref = list(itertools.accumulate(stones))
        # dp tracks the maximum score difference achievable
        # dp[i] = max(dp[i + 1], pref[i] - dp[i + 1])
        dp = pref[-1]
        for s in pref[-2:0:-1]:
            dp = max(dp, s - dp)
        return dp