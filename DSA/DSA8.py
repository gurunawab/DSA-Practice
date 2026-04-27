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

#Check if There is a Valid Path in a Grid
from collections import deque

def hasValidPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])

        move = {
            1:[(0, -1), (0, 1)], 2:[(-1, 0), (1, 0)],
            3:[(0, -1), (1, 0)], 4:[(0, 1), (1, 0)],
            5:[(0, -1), (-1, 0)], 6:[(0, 1), (-1, 0)]
        }

        q = deque([(0, 0)])
        visited = {(0, 0)}

        while q:
            r, c = q.popleft()
            if (r, c) == (R - 1, C - 1): return True

            for dr, dc in move[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    if (-dr, -dc) in move[grid[nr][nc]]:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return False