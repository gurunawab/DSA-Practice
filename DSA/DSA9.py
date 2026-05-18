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