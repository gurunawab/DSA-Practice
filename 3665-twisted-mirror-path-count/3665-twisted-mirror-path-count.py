class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n, MOD = len(grid), len(grid[0]), 1_000_000_007
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def advance(r, c, d):
            while 0 <= r < m and 0 <= c < n:
                if not grid[r][c]: return r, c
                d ^= 1
                r, c = (r, c + 1) if d == 0 else (r + 1, c)
            return -1, -1

        for i in range(m):
            for j in range(n):
                if not dp[i][j]: continue
                for nr, nc in (advance(i, j + 1, 0), advance(i + 1, j, 1)):
                    if nr != -1:
                        dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]