from collections import Counter

class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count, left, ans = Counter(), 0, 0

        for right, x in enumerate(nums):
            count[x] += 1
            while count[x] > k:
                count[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans