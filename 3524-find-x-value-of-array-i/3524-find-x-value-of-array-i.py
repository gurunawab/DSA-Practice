class Solution:

  def resultArray(self, nums: list[int], k: int) -> list[int]:
    res = [0] * k
    dp = [0] * k  # dp[rem] counts subarrays ending at previous index modulo k

    for x in nums:
      next_dp = [0] * k
      for rem in range(k):
        if dp[rem]:
          next_dp[(rem * x) % k] += dp[rem]
      next_dp[x % k] += 1  # Subarray starting at current index

      for rem in range(k):
        res[rem] += next_dp[rem]

      dp = next_dp

    return res