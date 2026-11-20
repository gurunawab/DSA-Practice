from collections import defaultdict
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        # dp[v] = longest consecutive sequence ending with value v
        dp = defaultdict(int)
        
        for x in nums:
            # Update x + 1 first so it doesn't reuse the current element x
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())