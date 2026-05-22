#Jump Game IV
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1: return 0
        
    
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([0])
        visited = {0}
        steps = 0
        
        while queue:
            
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx == n - 1: return steps
                
                
                next_indices = [idx - 1, idx + 1] + graph[arr[idx]]
                graph[arr[idx]] = [] 
                
                for nxt in next_indices:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            steps += 1  

#Minimum Multiplications to reach End
from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        if start == end:
            return 0
            
        MOD = 1000
        
        dist = [-1] * MOD
        
        queue = deque([start])
        dist[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for num in arr:
                next_node = (node * num) % MOD
                
                if dist[next_node] == -1:
                    dist[next_node] = dist[node] + 1
                    
                    if next_node == end:
                        return dist[next_node]
                        
                    queue.append(next_node)
                    
        return -1    

#Product Pair
def isProduct(self, arr, target):
        seen = set()
        
        for x in arr:
            if target == 0 and x == 0:
                if len(seen) > 0:
                    return True
                    
            elif target == 0:
                if 0 in seen:
                    return True
                    
            else:
                if x != 0 and target % x == 0:
                    complement = target // x
                    if complement in seen:
                        return True
                        
            seen.add(x)
            
        return False  

#Find the Prefix Common Array of Two Arrays
def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        C = []

        freq = [0] * (n + 1)

        common_count = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            C.append(common_count)

        return C 

#1s Surrounded by 0s
def cntOnes(self, grid):
        if not grid or not grid[0]:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != 1:
                return 
            
            grid[r][c] = 2
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for c in range(m):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[n-1][c] == 1:
                dfs(n - 1, c)
                
        for r in range(n):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][m-1] == 1:
                dfs(r, m - 1)
                
        trapped_ones = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    trapped_ones += 1
                    
        return trapped_ones   

#Search in Rotated Sorted Array
def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1                               