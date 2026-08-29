class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
       
        idx = sorted(range(n), key=lambda i: nums[i])
        ans = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
           
            while j < n and nums[idx[j]] - nums[idx[j-1]] <= limit:
                j += 1
                
           
            group_idx = sorted(idx[i:j])
            for k, original_i in enumerate(group_idx):
                ans[original_i] = nums[idx[i+k]]
            
            i = j
            
        return ans