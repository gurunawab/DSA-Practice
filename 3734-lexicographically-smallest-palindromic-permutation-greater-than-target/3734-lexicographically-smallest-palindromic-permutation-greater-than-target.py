from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odds = [c for c, cnt in counts.items() if cnt % 2]
        if len(odds) > 1:
            return ""
        
        mid = odds[0] if odds else ""
        half_counts = {c: cnt // 2 for c, cnt in counts.items()}
        half_len = len(s) // 2

        # 1. Check if matching target's first half exactly works
        t_first = target[:half_len]
        t_counts = Counter(t_first)
        if all(t_counts[c] <= half_counts.get(c, 0) for c in t_counts):
            candidate = t_first + mid + t_first[::-1]
            if candidate > target:
                return candidate

        # 2. Backtrack to find the longest matching prefix, then place a strictly larger char
        for i in range(half_len - 1, -1, -1):
            pref = target[:i]
            p_counts = Counter(pref)
            if any(p_counts[c] > half_counts.get(c, 0) for c in p_counts):
                continue
            
            rem = {c: half_counts[c] - p_counts[c] for c in half_counts}
            for char in sorted(rem):
                if char > target[i] and rem[char] > 0:
                    rem[char] -= 1
                    rest = "".join(c * rem[c] for c in sorted(rem))
                    half = pref + char + rest
                    return half + mid + half[::-1]
                    
        return ""