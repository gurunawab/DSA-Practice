#Detect Cycles in 2D Grid
def containsCycle(self, grid: List[List[str]]) -> bool:
        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc):
            visited.add((r, c))
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == grid[r][c]:
                    if (nr, nc) in visited:
                        if (nr, nc) != (pr, pc): return True
                    else:
                        if dfs(nr, nc, r, c): return True

            return False

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited:
                    if dfs(r, c, -1, -1): return True

        return False  