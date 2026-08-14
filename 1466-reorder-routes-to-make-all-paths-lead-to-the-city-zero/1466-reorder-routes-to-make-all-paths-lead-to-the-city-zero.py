class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append((v, 1))  # original direction (needs flip if moving outward from 0)
            g[v].append((u, 0))  # reverse direction (already points towards 0)
        
        q, visited, changes = [0], {0}, 0
        for u in q:
            for v, cost in g[u]:
                if v not in visited:
                    visited.add(v)
                    changes += cost
                    q.append(v)
        return changes