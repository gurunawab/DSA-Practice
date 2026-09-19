import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        ans = [-1] * len(queries)
        deferred = [[] for _ in heights]
        
        # Process base cases and store unresolved queries at max(a, b)
        for i, (a, b) in enumerate(queries):
            a, b = min(a, b), max(a, b)
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                deferred[b].append((heights[a], i))
        
        min_heap = []
        # Iterate through buildings to resolve queries offline
        for idx, h in enumerate(heights):
            while min_heap and min_heap[0][0] < h:
                ans[heapq.heappop(min_heap)[1]] = idx
            for target_h, q_idx in deferred[idx]:
                heapq.heappush(min_heap, (target_h, q_idx))
                
        return ans