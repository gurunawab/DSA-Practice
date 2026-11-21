class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_reparent(u: int):
            ch = s[u]
            prev = last_seen.get(ch)
            if prev is not None:
                new_parent[u] = prev
            last_seen[ch] = u
            
            for v in adj[u]:
                dfs_reparent(v)
                
            if prev is None:
                del last_seen[ch]
            else:
                last_seen[ch] = prev
                
        dfs_reparent(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]
            
        dfs_size(0)
        return ans