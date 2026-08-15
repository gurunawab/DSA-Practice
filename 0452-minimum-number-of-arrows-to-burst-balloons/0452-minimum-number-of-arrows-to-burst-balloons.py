class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows, last_end = 0, float("-inf")
        for start, end in points:
            if start > last_end:
                arrows += 1
                last_end = end
        return arrows