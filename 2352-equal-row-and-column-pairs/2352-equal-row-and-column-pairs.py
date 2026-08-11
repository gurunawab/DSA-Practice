class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = Counter(tuple(row) for row in grid)
        return sum(count[col] for col in zip(*grid))