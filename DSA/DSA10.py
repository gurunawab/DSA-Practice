#Count Sorted Digit Groupings
from functools import lru_cache

class Solution:
    def validGroups(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def solve(index, prev_sum):
            
            if index == n:
                return 1
            
            current_sum = 0
            ways = 0
            
           
            for j in range(index, n):
                current_sum += int(s[j])
                
                
                if current_sum >= prev_sum:
                    ways += solve(j + 1, current_sum)
                    
            return ways

       
        return solve(0, 0)