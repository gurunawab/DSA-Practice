class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack, cur, union = [], [""], []

        for ch in expression:
            if ch.isalpha():
                cur = [c + ch for c in cur]
            elif ch == '{':
                stack.append((union, cur))
                union, cur = [], [""]
            elif ch == ',':
                union.extend(cur)
                cur = [""]
            elif ch == '}':
                sub_res = union + cur
                prev_union, prev_cur = stack.pop()
                union = prev_union
                cur = [p + s for p in prev_cur for s in sub_res]

        return sorted(set(union + cur))