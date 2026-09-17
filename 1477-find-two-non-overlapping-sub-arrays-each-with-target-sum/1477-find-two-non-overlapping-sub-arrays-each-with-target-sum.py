class Solution:

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n, left, cur = len(arr), 0, 0
        dp = [float("inf")] * (n + 1)
        ans = best = float("inf")

        for right in range(n):
            cur += arr[right]
            while cur > target:
                cur -= arr[left]
                left += 1
            if cur == target:
                l = right - left + 1
                ans = min(ans, l + dp[left])
                best = min(best, l)
            dp[right + 1] = min(dp[right], best)

        return ans if ans != float("inf") else -1