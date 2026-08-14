class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n, q = len(maze), len(maze[0]), [(*entrance, 0)]
        maze[entrance[0]][entrance[1]] = '+'
        
        for r, c, d in q:
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr in (0, m - 1) or nc in (0, n - 1): 
                        return d + 1
                    maze[nr][nc] = '+'
                    q.append((nr, nc, d + 1))
                    
        return -1