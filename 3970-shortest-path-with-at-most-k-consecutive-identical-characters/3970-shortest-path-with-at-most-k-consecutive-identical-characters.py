import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
        
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        dist = {}
        # Heap state: (total_weight, current_node, consecutive_count)
        pq = [(0, 0, 1)]
        dist[(0, 1)] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > dist.get((u, count), float('inf')):
                continue
                
            for v, w in adj[u]:
                next_count = count + 1 if labels[v] == labels[u] else 1
                if next_count <= k and d + w < dist.get((v, next_count), float('inf')):
                    dist[(v, next_count)] = d + w
                    heapq.heappush(pq, (d + w, v, next_count))
                    
        return -1