class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()

        res = []
        for i in range(len(s), 0, -k):
            start = max(0, i - k)
            res.append(s[start:i])

        return '-'.join(res[::-1])    