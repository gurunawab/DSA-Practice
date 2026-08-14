import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = max_score = 0
        heap = []
        
        for n2, n1 in sorted(zip(nums2, nums1), reverse=True):
            heapq.heappush(heap, n1)
            total += n1
            
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, total * n2)
                
        return max_score