import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        seen, count = [], 0
        for x in nums:
            count += len(seen) - bisect.bisect_right(seen, 2 * x)
            bisect.insort(seen, x)
        return count