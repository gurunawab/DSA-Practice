class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res, r, step = [""] * numRows, 0, 1
        for c in s:
            res[r] += c
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step
        return "".join(res)