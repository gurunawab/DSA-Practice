class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        g = [["#"] * n for _ in range(m)]
        for j in range(n):
            g[0][j] = "."
        for i in range(m):
            g[i][n - 1] = "."
        return ["".join(r) for r in g] 