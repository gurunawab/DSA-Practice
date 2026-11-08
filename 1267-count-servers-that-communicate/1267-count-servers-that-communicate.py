class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [sum(row) for row in grid]
        col_count = [sum(grid[r][c] for r in range(m)) for c in range(n)]

        return sum(
            grid[r][c]
            for r in range(m)
            for c in range(n)
            if grid[r][c] and (row_count[r] > 1 or col_count[c] > 1)
        )