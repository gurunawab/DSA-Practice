class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            current_take = 0
            
            for X in range(1, 4):
                if i + X - 1 < n:
                    current_take += stoneValue[i + X - 1]
                    score_diff = current_take - dp[(i + X) % 4]
                    max_diff = max(max_diff, score_diff)
            
            dp[i % 4] = max_diff
        
        alice_diff = dp[0]
        
        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"  