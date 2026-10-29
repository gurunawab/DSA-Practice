class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        up = [[0] * 17 for _ in range(n)]
        tin, tout, depth = [0] * n, [0] * n, [0] * n
        timer, chars = 0, [ord(c) - 97 for c in s]

        # Iterative DFS to avoid recursion limits
        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                up[u][0] = p
                for i in range(1, 17):
                    up[u][i] = up[up[u][i - 1]][i - 1]
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        def lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            for i in range(16, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v: return u
            for i in range(16, -1, -1):
                if up[u][i] != up[v][i]:
                    u, v = up[u][i], up[v][i]
            return up[u][0]

        bit = [0] * (n + 2)
        def add(i, val):
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def query(i):
            ans = 0
            while i > 0:
                ans ^= bit[i]
                i -= i & -i
            return ans

        def update_node(u, val):
            add(tin[u], val)
            add(tout[u] + 1, val)

        for u in range(n):
            update_node(u, 1 << chars[u])

        res = []
        for q in queries:
            t, a, b = q.split()
            if t == "update":
                u, new_val = int(a), ord(b) - 97
                diff = (1 << chars[u]) ^ (1 << new_val)
                chars[u] = new_val
                update_node(u, diff)
            else:
                u, v = int(a), int(b)
                anc = lca(u, v)
                mask = query(tin[u]) ^ query(tin[v]) ^ (1 << chars[anc])
                res.append((mask & (mask - 1)) == 0)

        return res  