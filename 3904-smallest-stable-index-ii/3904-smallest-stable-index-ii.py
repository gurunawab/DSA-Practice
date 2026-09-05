from itertools import accumulate

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pref_max = list(accumulate(nums, max))
        suff_min = list(accumulate(reversed(nums), min))[::-1]
        return next((i for i, (mx, mn) in enumerate(zip(pref_max, suff_min)) if mx - mn <= k), -1)