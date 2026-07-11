from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_count = 0
        
        for i in range(n):
            if not visited[i]:
                
                component = []
                stack = [i]
                visited[i] = True
                while stack:
                    u = stack.pop()
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                
                
                v_count = len(component)
                e_count = 0
                for node in component:
                    e_count += len(adj[node])
                
               
                if e_count == v_count * (v_count - 1):
                    complete_count += 1
                    
        return complete_count