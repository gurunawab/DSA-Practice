class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        
        dp_sum = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
     
        dp_sum[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1
        
     
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                
             
                for dx, dy in [(0, 1), (1, 0), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if ni < n and nj < n and dp_sum[ni][nj] != -1:
                       
                        val = 0 if board[i][j] == 'E' else int(board[i][j])
                        new_sum = dp_sum[ni][nj] + val
                        
                        if new_sum > dp_sum[i][j]:
                            dp_sum[i][j] = new_sum
                            dp_count[i][j] = dp_count[ni][nj]
                        elif new_sum == dp_sum[i][j]:
                            dp_count[i][j] = (dp_count[i][j] + dp_count[ni][nj]) % MOD
                            
        result_sum = max(0, dp_sum[0][0])
        result_count = dp_count[0][0] if dp_sum[0][0] != -1 else 0
        
        return [result_sum, result_count]