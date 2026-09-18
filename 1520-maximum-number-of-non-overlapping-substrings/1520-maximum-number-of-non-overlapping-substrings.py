class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}

        intervals = []
        for ch in first:
            l, r = first[ch], last[ch]
            valid = True
            i = l
            while i <= r:
                c = s[i]
                if first[c] < l:  # Extended before current start
                    valid = False
                    break
                r = max(r, last[c])
                i += 1
            if valid:
                intervals.append((r, l))

        # Greedy selection by earliest ending position
        intervals.sort()
        res = []
        prev_end = -1
        for r, l in intervals:
            if l > prev_end:
                res.append(s[l : r + 1])
                prev_end = r

        return res  