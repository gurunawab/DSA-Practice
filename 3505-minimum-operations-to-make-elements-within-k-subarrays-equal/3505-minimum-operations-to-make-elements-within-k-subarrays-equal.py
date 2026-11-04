import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        k_left = (x + 1) // 2
        k_right = x // 2
        
        max_heap = []  # -val (left half)
        min_heap = []  # val (right half)
        delayed = defaultdict(int)
        
        sum_left = 0
        sum_right = 0
        size_left = 0
        size_right = 0

        def prune(heap, is_max):
            while heap:
                val = -heap[0] if is_max else heap[0]
                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal size_left, size_right, sum_left, sum_right
            while size_left < k_left and min_heap:
                prune(min_heap, False)
                val = heapq.heappop(min_heap)
                sum_right -= val
                size_right -= 1
                heapq.heappush(max_heap, -val)
                sum_left += val
                size_left += 1

            while size_left > k_left:
                prune(max_heap, True)
                val = -heapq.heappop(max_heap)
                sum_left -= val
                size_left -= 1
                heapq.heappush(min_heap, val)
                sum_right += val
                size_right += 1

            prune(max_heap, True)
            prune(min_heap, False)

        def add(num):
            nonlocal size_left, size_right, sum_left, sum_right
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                sum_left += num
                size_left += 1
            else:
                heapq.heappush(min_heap, num)
                sum_right += num
                size_right += 1
            rebalance()

        def remove(num):
            nonlocal size_left, size_right, sum_left, sum_right
            delayed[num] += 1
            if num <= -max_heap[0]:
                sum_left -= num
                size_left -= 1
                if num == -max_heap[0]:
                    prune(max_heap, True)
            else:
                sum_right -= num
                size_right -= 1
                if min_heap and num == min_heap[0]:
                    prune(min_heap, False)
            rebalance()

        def get_cost():
            median = -max_heap[0]
            return (size_left * median - sum_left) + (sum_right - size_right * median)

        num_windows = n - x + 1
        cost = [0] * num_windows

        for i in range(x):
            add(nums[i])
        cost[0] = get_cost()

        for i in range(1, num_windows):
            remove(nums[i - 1])
            add(nums[i + x - 1])
            cost[i] = get_cost()

        # DP: dp_table[i][j] = index i tak j subarrays lene ki min cost
        dp_table = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp_table[0][0] = 0

        for i in range(n):
            for j in range(k + 1):
                if dp_table[i][j] == float('inf'):
                    continue
                # Option 1: Index i ko skip karo
                if dp_table[i][j] < dp_table[i + 1][j]:
                    dp_table[i + 1][j] = dp_table[i][j]

                # Option 2: Yahan se subarray nums[i : i + x] uthao
                if j < k and i + x <= n:
                    total = dp_table[i][j] + cost[i]
                    if total < dp_table[i + x][j + 1]:
                        dp_table[i + x][j + 1] = total

        return dp_table[n][k]