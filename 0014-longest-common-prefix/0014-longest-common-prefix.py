class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s1, s2 = min(strs), max(strs)
        for i, char in enumerate(s1):
            if char != s2[i]:
                return s1[:i]
        return s1