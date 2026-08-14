import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h1, h2 = costs[:candidates], costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(h1)
        heapq.heapify(h2)
        
        i, j = candidates, len(costs) - candidates - 1
        ans = 0
        
        for _ in range(k):
            if not h2 or (h1 and h1[0] <= h2[0]):
                ans += heapq.heappop(h1)
                if i <= j:
                    heapq.heappush(h1, costs[i])
                    i += 1
            else:
                ans += heapq.heappop(h2)
                if i <= j:
                    heapq.heappush(h2, costs[j])
                    j -= 1
                    
        return ans