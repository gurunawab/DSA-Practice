from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = max_freq = 0
        
        for r, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])
            
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
        return len(s) - l