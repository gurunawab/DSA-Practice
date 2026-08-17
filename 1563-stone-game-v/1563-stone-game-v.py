class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                total = pref[j + 1] - pref[i]
                
                # Maintain two-pointer split to optimize range queries
                while pref[mid + 1] - pref[i] < total - (pref[mid + 1] - pref[i]):
                    mid += 1
                
                s = pref[mid + 1] - pref[i]
                if s * 2 == total:
                    res = max(max_l[i][mid], max_r[mid + 1][j])
                else:
                    left_part = max_l[i][mid - 1] if mid > i else 0
                    right_part = max_r[mid + 1][j] if mid < j else 0
                    res = max(left_part, right_part)
                
                dp[i][j] = res
                max_l[i][j] = max(max_l[i][j - 1], res + total)
                max_r[i][j] = max(max_r[i + 1][j], res + total)

        return dp[0][n - 1]