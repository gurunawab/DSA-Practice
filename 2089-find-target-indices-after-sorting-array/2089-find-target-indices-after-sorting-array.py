class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, x in enumerate(sorted(nums)) if x == target]