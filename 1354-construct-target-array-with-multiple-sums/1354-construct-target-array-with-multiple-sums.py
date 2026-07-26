import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        if len(target) == 1:
            return target[0] == 1

        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            largest = -heapq.heappop(max_heap)
            rest_sum = total_sum - largest

           
            if largest == 1 or rest_sum == 1:
                return True

           
            if largest <= rest_sum or rest_sum == 0 or largest % rest_sum == 0:
                return False

            
            prev = largest % rest_sum
            total_sum = rest_sum + prev
            heapq.heappush(max_heap, -prev)