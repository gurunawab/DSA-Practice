class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        # Check every consecutive pair of characters (0-1, 2-3, 4-5, ...)
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes