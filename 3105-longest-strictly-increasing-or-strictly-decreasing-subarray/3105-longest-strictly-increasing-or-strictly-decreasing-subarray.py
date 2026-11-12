class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc, dec = inc + 1, 1
            elif nums[i] < nums[i - 1]:
                inc, dec = 1, dec + 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans