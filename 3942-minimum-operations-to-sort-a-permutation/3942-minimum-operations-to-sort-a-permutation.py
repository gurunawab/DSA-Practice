class Solution:

  def minOperations(self, nums: List[int]) -> int:
    n, k = len(nums), nums.index(0)

    if all(nums[i] == (i - k) % n for i in range(n)):
      return min(k, n - k + 2)

    if all(nums[i] == (k - i) % n for i in range(n)):
      return min(n - k, (k + 1) % n + 1)

    return -1