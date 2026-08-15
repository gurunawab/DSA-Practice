class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals, last_end = 0, float("-inf")
        for start, end in intervals:
            if start < last_end:
                removals += 1
            else:
                last_end = end
        return removals