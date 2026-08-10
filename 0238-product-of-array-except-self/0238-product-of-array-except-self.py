class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, prefix, suffix = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            res[~i] *= suffix
            suffix *= nums[~i]
        return res