class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0
        
        for i in range(n):
            
            multiplier = (i // 8) + 1
            pushes += multiplier
            
        return pushes