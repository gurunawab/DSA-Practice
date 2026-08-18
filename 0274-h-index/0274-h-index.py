class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(c > i for i, c in enumerate(sorted(citations, reverse=True)))