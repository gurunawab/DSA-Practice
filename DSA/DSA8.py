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

#Maximum Path Score in a Grid
def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        memo = {}

        def solve(r, c, rem_k):
            if r == m or c == n or rem_k < 0:
                return float('-inf')

            val = grid[r][c]
            score = val if val != 0 else 0
            cost = 1 if val > 0 else 0

            new_rem_k = rem_k - cost
            if new_rem_k < 0: return float('-inf')

            if r == m - 1 and c == n - 1:
                return score

            state = (r, c, rem_k)
            if state in memo: return memo[state]

            res = score + max(solve(r + 1, c, new_rem_k), solve(r, c + 1, new_rem_k))

            memo[state] = res
            return res

        result = solve(0, 0, k)
        return result if result > float('-inf') else -1 

#Kth Largest in a Stream
import heapq
def kthLargest(self, arr, k):
    
        min_heap = []
        result = []
        
        for num in arr:

            heapq.heappush(min_heap, num)
            
          
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
 
            if len(min_heap) < k:

                result.append(-1)
            else:
              
                result.append(min_heap[0])
                
        return result