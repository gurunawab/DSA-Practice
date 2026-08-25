class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        ans = k
        while ans in s:
            ans += k
        return ans