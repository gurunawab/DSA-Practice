from math import gcd, lcm

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            p, g, l = 1, 0, 1
            for j in range(i, len(nums)):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g * l:
                    ans = max(ans, j - i + 1)
        return ans