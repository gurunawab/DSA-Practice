class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = math.ceil(len(b) / len(a))

        if b in a * count:
            return count

        if b in a * (count + 1):
            return count + 1

        return -1        