class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mn, mx = min(need1, need2), max(need1, need2)
        rem_cost = cost1 if need1 > need2 else cost2
        return min(
            need1 * cost1 + need2 * cost2,
            mn * costBoth + (mx - mn) * rem_cost,
            mx * costBoth
        )