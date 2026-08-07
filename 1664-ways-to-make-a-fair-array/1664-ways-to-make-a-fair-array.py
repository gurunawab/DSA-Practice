class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right = [sum(nums[0::2]), sum(nums[1::2])]
        left = [0, 0]
        ans = 0
        
        for i, num in enumerate(nums):
            right[i % 2] -= num
            ans += (left[0] + right[1] == left[1] + right[0])
            left[i % 2] += num
            
        return ans