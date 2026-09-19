class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k > 0:
            # Count steps between prefix curr and curr + 1 up to n
            steps, first, last = 0, curr, curr + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            
            # Move to next sibling if steps fit inside k, else move to child
            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr