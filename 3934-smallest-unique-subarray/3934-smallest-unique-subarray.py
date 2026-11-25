from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Double hashing constants to avoid collisions
        M1, M2 = 10**9 + 7, 10**9 + 9
        B1, B2 = 1315423911, 2654435761

        def has_unique(L: int) -> bool:
            h1 = h2 = 0
            p1 = pow(B1, L, M1)
            p2 = pow(B2, L, M2)
            counts = Counter()

            for i, x in enumerate(nums):
                h1 = (h1 * B1 + x) % M1
                h2 = (h2 * B2 + x) % M2
                if i >= L:
                    h1 = (h1 - nums[i - L] * p1) % M1
                    h2 = (h2 - nums[i - L] * p2) % M2
                if i >= L - 1:
                    counts[(h1, h2)] += 1

            return any(c == 1 for c in counts.values())

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo