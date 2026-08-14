class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -float('inf')
        for p in prices:
            cash, hold = max(cash, hold + p - fee), max(hold, cash - p)
        return cash