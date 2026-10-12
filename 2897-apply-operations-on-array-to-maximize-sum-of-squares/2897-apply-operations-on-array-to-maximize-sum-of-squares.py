class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        count = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    count[i] += 1
        
        MOD = 10**9 + 7
        ans = 0
        for _ in range(k):
            val = 0
            for i in range(32):
                if count[i] > 0:
                    val |= 1 << i
                    count[i] -= 1
            ans = (ans + val * val) % MOD
            
        return ans