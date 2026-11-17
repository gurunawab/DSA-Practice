from functools import cache

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute minimum changes to make s[i:j] a semi-palindrome
        cost = [[float('inf')] * (n + 1) for _ in range(n)]
        
        for length in range(2, n + 1):
            divs = [d for d in range(1, length) if length % d == 0]
            for i in range(n - length + 1):
                j = i + length
                best = float('inf')
                for d in divs:
                    changes = 0
                    for rem in range(d):
                        l, r = i + rem, j - d + rem
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best

        # DP to partition s into k substrings
        @cache
        def dp(idx: int, rem_k: int) -> int:
            if rem_k == 1:
                return cost[idx][n]
            res = float('inf')
            # Each remaining substring must have length >= 2
            for nxt in range(idx + 2, n - 2 * (rem_k - 1) + 1):
                res = min(res, cost[idx][nxt] + dp(nxt, rem_k - 1))
            return res

        return dp(0, k)