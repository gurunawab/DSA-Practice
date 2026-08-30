class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        l, r = sorted([nums.index(min(nums)), nums.index(max(nums))])
        n = len(nums)
        return min(r + 1, n - l, (l + 1) + (n - r))