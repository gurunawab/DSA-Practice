class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, k = 0, 1
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left  