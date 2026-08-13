class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)

        def merge(L, R):
            p1, s1, m1, cl1, cr1, sz1 = L
            p2, s2, m2, cl2, cr2, sz2 = R
            cross = s1 + p2 if cr1 == cl2 else 0
            p = p1 + p2 if p1 == sz1 and cr1 == cl2 else p1
            s = s1 + s2 if s2 == sz2 and cr1 == cl2 else s2
            return (p, s, max(m1, m2, cross), cl1, cr2, sz1 + sz2)

        def build(i, l, r):
            if l == r:
                tree[i] = (1, 1, 1, s[l], s[l], 1)
                return
            mid = (l + r) // 2
            build(2 * i, l, mid)
            build(2 * i + 1, mid + 1, r)
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(i, l, r, idx, ch):
            if l == r:
                tree[i] = (1, 1, 1, ch, ch, 1)
                return
            mid = (l + r) // 2
            if idx <= mid: update(2 * i, l, mid, idx, ch)
            else: update(2 * i + 1, mid + 1, r, idx, ch)
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        build(1, 0, n - 1)
        res = []
        for idx, ch in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, ch)
            res.append(tree[1][2])
        return res