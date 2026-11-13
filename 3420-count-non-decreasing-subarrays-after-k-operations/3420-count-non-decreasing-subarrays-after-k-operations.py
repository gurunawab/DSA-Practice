from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()  # Stores [max_val, count] in strictly decreasing order
        ops = 0
        ans = 0
        j = n - 1
        
        for i in range(n - 1, -1, -1):
            cnt = 1
            # Merge smaller elements to the right up to nums[i]
            while dq and dq[0][0] < nums[i]:
                val, c = dq.popleft()
                ops += (nums[i] - val) * c
                cnt += c
            dq.appendleft([nums[i], cnt])
            
            # Shrink window from the right if operations exceed k
            while ops > k:
                ops -= dq[-1][0] - nums[j]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                j -= 1
                
            ans += j - i + 1
            
        return ans