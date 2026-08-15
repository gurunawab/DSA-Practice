class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if not any(nums):
            return 0
        return len(nums) if reduce(xor, nums) else len(nums) - 1