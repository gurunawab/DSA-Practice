class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == target:
                    return curr
                if abs(curr - target) < abs(closest - target):
                    closest = curr
                if curr < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest