class Solution:

  def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
    def kadane(A):
      curr = ans = 0
      for x in A:
        curr = max(0, curr + x)
        ans = max(ans, curr)
      return ans

    MOD = 10**9 + 7
    if k == 1:
      return kadane(arr) % MOD
    return (
        kadane(arr * 2) + max(0, sum(arr)) * (k - 2)
    ) % MOD