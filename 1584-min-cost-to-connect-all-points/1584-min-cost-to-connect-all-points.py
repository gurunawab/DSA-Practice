import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n, visited, min_heap, total_cost = len(points), set(), [(0, 0)], 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            
            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    heapq.heappush(min_heap, (abs(x1 - x2) + abs(y1 - y2), v))
                    
        return total_cost