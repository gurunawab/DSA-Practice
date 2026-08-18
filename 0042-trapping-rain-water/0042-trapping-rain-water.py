class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, max_l, max_r, ans = 0, len(height) - 1, 0, 0, 0
        while l < r:
            if height[l] <= height[r]:
                max_l = max(max_l, height[l])
                ans += max_l - height[l]
                l += 1
            else:
                max_r = max(max_r, height[r])
                ans += max_r - height[r]
                r -= 1
        return ans