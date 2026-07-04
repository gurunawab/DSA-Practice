from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        min_weight = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in adj[node]:
               
                min_weight = min(min_weight, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_weight