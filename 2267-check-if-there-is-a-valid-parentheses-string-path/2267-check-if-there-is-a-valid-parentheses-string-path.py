class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(': 
            return False

        @functools.cache
        def dfs(r, c, bal):
            bal += 1 if grid[r][c] == '(' else -1
            if bal < 0 or bal > (m + n - 1 - r - c): 
                return False
            if r == m - 1 and c == n - 1: 
                return bal == 0
            
            return (r + 1 < m and dfs(r + 1, c, bal)) or (c + 1 < n and dfs(r, c + 1, bal))

        return dfs(0, 0, 0)