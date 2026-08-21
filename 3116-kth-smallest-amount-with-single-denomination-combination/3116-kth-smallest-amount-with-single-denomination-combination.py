import bisect, math
from itertools import combinations


class Solution:

    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        subsets = [
            ((-1) ** (r + 1), math.lcm(*comb))
            for r in range(1, n + 1)
            for comb in combinations(coins, r)
        ]

        def count(x):
            return sum(sign * (x // l) for sign, l in subsets)

        return bisect.bisect_left(range(min(coins) * k + 1), k, key=count)