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