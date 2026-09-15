class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans, last = 0, 0
        for i in range(len(s)):
            for l in (k, k + 1):
                start = i - l + 1
                if start >= last and s[start : i + 1] == s[start : i + 1][::-1]:
                    ans += 1
                    last = i + 1
                    break
        return ans