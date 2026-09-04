class Solution:

  def firstStableIndex(self, nums: list[int], k: int) -> int:
    suffix_min = nums[:]
    for i in range(len(nums) - 2, -1, -1):
      suffix_min[i] = min(suffix_min[i], suffix_min[i + 1])

    prefix_max = 0
    for i, num in enumerate(nums):
      prefix_max = max(prefix_max, num)
      if prefix_max - suffix_min[i] <= k:
        return i

    return -1