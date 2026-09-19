class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Store original indices
        sorted_edges = sorted(enumerate(edges), key=lambda x: x[1][2])

        def get_mst_weight(skip_edge=-1, force_edge=-1):
            uf = UnionFind(n)
            weight, count = 0, 0
            if force_edge != -1:
                u, v, w = edges[force_edge]
                uf.union(u, v)
                weight += w
                count += 1
            for idx, (u, v, w) in sorted_edges:
                if idx == skip_edge:
                    continue
                if uf.union(u, v):
                    weight += w
                    count += 1
            return weight if count == n - 1 else float('inf')

        base_mst = get_mst_weight()
        critical, pseudo = [], []

        for i in range(len(edges)):
            if get_mst_weight(skip_edge=i) > base_mst:
                critical.append(i)
            elif get_mst_weight(force_edge=i) == base_mst:
                pseudo.append(i)

        return [critical, pseudo]