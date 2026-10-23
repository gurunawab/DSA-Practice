class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = None
        for i, val in enumerate(nums):
            if val != i:
                k = val if k is None else (k & val)
        return k if k is not None else 0