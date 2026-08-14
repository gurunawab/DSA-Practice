class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        time = 0
        
        while fresh and rotten:
            rotten = {(r + dr, c + dc) for r, c in rotten for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)) if (r + dr, c + dc) in fresh}
            fresh -= rotten
            time += 1
            
        return -1 if fresh else time