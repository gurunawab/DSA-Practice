class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(len(set(nums[i:j])) ** 2 for i in range(n) for j in range(i + 1, n + 1))