class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(part: str) -> bool:
            return 0 <= int(part) <= 255 and (part == "0" or not part.startswith("0"))

        return [
            f"{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}"
            for i in range(1, 4)
            for j in range(i + 1, i + 4)
            for k in range(j + 1, j + 4)
            if k < len(s) and all(valid(part) for part in (s[:i], s[i:j], s[j:k], s[k:]))
        ]