class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        
        dp0, dp1, dp2 = 0, float("inf"), float("inf")

        for c in costs:
            
            cur = c + min(dp0 + 1, dp1 + 4, dp2 + 9)
            dp0, dp1, dp2 = cur, dp0, dp1

        return dp0