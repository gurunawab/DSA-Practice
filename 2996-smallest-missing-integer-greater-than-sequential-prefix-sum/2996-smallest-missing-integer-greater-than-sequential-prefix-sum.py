class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
            
        s, seen = sum(nums[:i]), set(nums)
        while s in seen:
            s += 1
            
        return s