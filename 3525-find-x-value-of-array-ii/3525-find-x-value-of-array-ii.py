class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]

        def merge(p1, c1, p2, c2):
            cnt = list(c1)
            for r in range(k):
                cnt[(p1 * r) % k] += c2[r]
            return (p1 * p2) % k, cnt

        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                tree_prod[node] = val
                tree_cnt[node][val] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree_prod[node], tree_cnt[node] = merge(
                tree_prod[2 * node], tree_cnt[2 * node],
                tree_prod[2 * node + 1], tree_cnt[2 * node + 1]
            )

        def update(node, l, r, idx, val):
            if l == r:
                tree_prod[node] = val % k
                tree_cnt[node] = [0] * k
                tree_cnt[node][val % k] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            tree_prod[node], tree_cnt[node] = merge(
                tree_prod[2 * node], tree_cnt[2 * node],
                tree_prod[2 * node + 1], tree_cnt[2 * node + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
            p1, c1 = query(2 * node, l, mid, ql, qr)
            p2, c2 = query(2 * node + 1, mid + 1, r, ql, qr)
            return merge(p1, c1, p2, c2)

        build(1, 0, n - 1)
        res = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, cnt = query(1, 0, n - 1, start, n - 1)
            res.append(cnt[x])

        return res