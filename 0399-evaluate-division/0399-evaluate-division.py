class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(dict)
        for (u, v), val in zip(equations, values):
            g[u][v], g[v][u] = val, 1.0 / val

        def dfs(u, target, visited):
            if u not in g or target not in g: return -1.0
            if u == target: return 1.0
            visited.add(u)
            for v, val in g[u].items():
                if v not in visited:
                    res = dfs(v, target, visited)
                    if res != -1.0: return val * res
            return -1.0

        return [dfs(u, v, set()) for u, v in queries]