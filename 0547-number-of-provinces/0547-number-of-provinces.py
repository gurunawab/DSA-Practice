class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited, count = set(), 0
        def dfs(i):
            visited.add(i)
            [dfs(j) for j, adj in enumerate(isConnected[i]) if adj and j not in visited]
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        return count     