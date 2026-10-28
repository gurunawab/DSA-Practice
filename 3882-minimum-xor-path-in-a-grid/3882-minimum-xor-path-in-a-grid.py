class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for j in range(1, n):
            dp[j] = {x ^ grid[0][j] for x in dp[j - 1]}
            
        for i in range(1, m):
            dp[0] = {x ^ grid[i][0] for x in dp[0]}
            for j in range(1, n):
                dp[j] = {x ^ grid[i][j] for x in (dp[j] | dp[j - 1])}
                
        return min(dp[-1])