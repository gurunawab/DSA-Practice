class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        return sum((nums[i] != nums[i - 1]) * (len(nums) - i) for i in range(1, len(nums)))