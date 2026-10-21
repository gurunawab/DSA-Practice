class Solution:
    def minOperations(self, s: str) -> int:
        target = "".join(sorted(s))
        if s == target: return 0
        if len(s) == 2: return -1
        
        # 1 op if sorting a proper prefix or proper suffix is enough
        if s[0] == target[0] and sorted(s[1:]) == list(target[1:]): return 1
        if s[-1] == target[-1] and sorted(s[:-1]) == list(target[:-1]): return 1
        
        # 3 ops if the globally smallest character is at the very end AND 
        # the globally largest character is at the very start (worst case rotation)
        mn, mx = target[0], target[-1]
        if s[0] == mx and s[-1] == mn and mn != mx:
            if s.count(mn) == 1 and s.count(mx) == 1:
                return 3
        
        # Otherwise, 2 operations (prefix then suffix or vice versa) are always sufficient
        return 2