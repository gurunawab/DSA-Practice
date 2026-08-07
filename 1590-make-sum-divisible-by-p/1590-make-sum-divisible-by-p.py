class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0: return 0
        
        seen = {0: -1}
        cur, res = 0, len(nums)
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            needed = (cur - target) % p
            if needed in seen:
                res = min(res, i - seen[needed])
            seen[cur] = i
            
        return res if res < len(nums) else -1