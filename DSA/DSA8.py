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

#Minimum Jumps to Reach End via Prime Teleportation
from collections import deque

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        
        val_to_indices = {}
        for i, v in enumerate(nums):
            val_to_indices.setdefault(v, []).append(i)

       
        max_n = max(nums)
        is_p = [True] * (max_n + 1)
        for p in range(2, int(max_n**0.5) + 1):
            if is_p[p]:
                for i in range(p*p, max_n + 1, p): is_p[i] = False

       
        q = deque([(0, 0)])
        v_idx, v_prime = {0}, set()
        
        while q:
            curr, d = q.popleft()
            if curr == n - 1: return d
            
            
            for nxt in [curr-1, curr+1]:
                if 0 <= nxt < n and nxt not in v_idx:
                    v_idx.add(nxt); q.append((nxt, d + 1))
            
          
            p = nums[curr]
            if p > 1 and is_p[p] and p not in v_prime:
                v_prime.add(p)
                
                for mult in range(p, max_n + 1, p):
                    if mult in val_to_indices:
                        for nxt in val_to_indices[mult]:
                            if nxt not in v_idx:
                                v_idx.add(nxt); q.append((nxt, d + 1))
                        del val_to_indices[mult] 
        return -1      

#Remove Invalid Parentheses
from collections import deque

class Solution:
    def validParenthesis(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
            
        if not s:
            return [""]
            
        queue = deque([s])
        visited = {s}
        result = []
        found = False
        
        while queue:
            level_size = len(queue)
            current_level_valid = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if is_valid(curr):
                    current_level_valid.append(curr)
                    found = True
                    
                if not found:
                    for i in range(len(curr)):
                        if curr[i] not in "()":
                            continue
                        
                        next_str = curr[:i] + curr[i+1:]
                        if next_str not in visited:
                            visited.add(next_str)
                            queue.append(next_str)
                            
            if found:
                result = sorted(list(set(current_level_valid)))
                break
            
        return result if result else [""]       

#Count Spanning Trees in a Graph
def countSpanTree(self, n, edges):
        if n <= 1:
            return 1
            
        laplacian = [[0] * n for _ in range(n)]
        
        for u, v in edges:
            laplacian[u][u] += 1
            laplacian[v][v] += 1
            laplacian[u][v] -= 1
            laplacian[v][u] -= 1
            
        size = n - 1
        adj = [row[:size] for row in laplacian[:size]]
        
        det = 1.0
        for i in range(size):
            pivot = i
            while pivot < size and abs(adj[pivot][i]) < 1e-9:
                pivot += 1
                
            if pivot == size:
                return 0
                
            if pivot != i:
                adj[i], adj[pivot] = adj[pivot], adj[i]
                det *= -1
                
            det *= adj[i][i]
            
            for j in range(i + 1, size):
                factor = adj[j][i] / adj[i][i]
                for k in range(i + 1, size):
                    adj[j][k] -= factor * adj[i][k]
                    
        return int(round(abs(det)))  

#Cyclically Rotating a Grid
def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2

        for layer in range(num_layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            elements = []

            for j in range(left, right):
                elements.append(grid[top][j])

            for i in range(top, bottom):
                elements.append(grid[i][right])

            for j in range(right, left, -1):
                elements.append(grid[bottom][j])

            for i in range(bottom, top, -1):
                elements.append(grid[i][left])

            L = len(elements)
            net_k = k % L

            rotated = elements[net_k:] + elements[:net_k]

            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1


        return grid

 #Max Profit from Two Machines
def maxProfit(self, x, y, a, b):
        n = len(a)
        
        tasks = []
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))
            
        tasks.sort(key=lambda x: x[0], reverse=True)
        
        total_profit = 0
        count_a = 0
        count_b = 0
        
        for diff, profit_a, profit_b in tasks:
            if profit_a >= profit_b:
                if count_a < x:
                    total_profit += profit_a
                    count_a += 1
                else:
                    total_profit += profit_b
                    count_b += 1
                    
            else:
                if count_b < y:
                    total_profit += profit_b
                    count_b += 1
                else:
                    total_profit += profit_a
                    count_a += 1
                    
        return total_profit            
