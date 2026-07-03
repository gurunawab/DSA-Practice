import heapq
from collections import defaultdict

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)
        all_costs = set()
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                all_costs.add(cost)
        
        sorted_costs = sorted(list(all_costs))
        
        def can_reach(min_allowed_cost):
           
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue
                if u == n - 1: return d <= k
                
                for v, cost in adj[u]:
                    if cost >= min_allowed_cost:
                        if dist[v] > d + cost:
                            dist[v] = d + cost
                            heapq.heappush(pq, (dist[v], v))
            return dist[n-1] <= k

        low = 0
        high = len(sorted_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach(sorted_costs[mid]):
                ans = sorted_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans   