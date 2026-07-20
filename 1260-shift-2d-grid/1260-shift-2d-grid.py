class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total = m * n
        
       
        res = [[0] * n for _ in range(m)]
        
       
        k = k % total
        
        for r in range(m):
            for c in range(n):
              
                old_pos = r * n + c
                
               
                new_pos = (old_pos + k) % total
                
                
                new_r = new_pos // n
                new_c = new_pos % n
                
                res[new_r][new_c] = grid[r][c]
                
        return res