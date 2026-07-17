import bisect
from typing import List

class Solution(object):
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
       
        multiples_count = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for i in range(g, max_val + 1, g):
                multiples_count[g] += counts[i]
                
       
        exact_gcd = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            c = multiples_count[g]
            total_pairs = c * (c - 1) // 2
            
            
            for i in range(2 * g, max_val + 1, g):
                total_pairs -= exact_gcd[i]
                
            exact_gcd[g] = total_pairs
            
        
        prefix_sums = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            prefix_sums[g] = prefix_sums[g - 1] + exact_gcd[g]
            
    
        ans = []
        for q in queries:
            
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans