from collections import Counter


class Solution:

  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    dp = {0: 1}
    for x in nums:
      dp = Counter({s + x: c for s, c in dp.items()}) + Counter(
          {s - x: c for s, c in dp.items()}
      )
    return dp[target]