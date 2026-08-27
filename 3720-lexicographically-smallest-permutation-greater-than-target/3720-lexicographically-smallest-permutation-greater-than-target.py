class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = collections.Counter(s)
        pref_counts = [count.copy()]
        
        # Build prefix frequency snapshots
        for ch in target:
            if count[ch] == 0:
                break
            count[ch] -= 1
            pref_counts.append(count.copy())
            
        # Check from the longest possible matching prefix down to 0
        for i in range(len(pref_counts) - 1, -1, -1):
            if i >= len(target):
                continue
            cnt = pref_counts[i]
            # Find the smallest character greater than target[i]
            for c in sorted(cnt):
                if c > target[i] and cnt[c] > 0:
                    cnt[c] -= 1
                    rest = "".join(sorted(cnt.elements()))
                    return target[:i] + c + rest
                    
        return ""