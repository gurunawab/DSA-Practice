import math

def isprime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= math.sqrt(n):
        if n % i ==0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    n = 7
    if(isprime(n)):
        print("true")
    else:
        print("false")    



def sieve(n):

    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:

            for i in range(p * p, n + 1, p):
                prime[i] = False

        p += 1

    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)

    return res

if __name__ == "__main__":
  n = 35  
  res = sieve(n)
  for ele in res:
      print(ele, end=' ')     


#Construct Product Matrix
def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        p = [[1 for _ in range(m)] for _ in range(n)]

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return p 


#Course Schedule I
def canFinish(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
            
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == n 


#Equal Sum Grid Partition I
def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])

        total_sum = 0
        for r in range(rows):
            for c in range(cols):
                total_sum += grid[r][c]
        
        if total_sum % 2 != 0:
            target = -1
        else:
            target = total_sum // 2

        current_row_sum = 0

        for r in range(rows - 1):
            for c in range(cols):
                current_row_sum += grid[r][c]

            if current_row_sum == target:
                return True

        current_col_sum = 0
        for c in range(cols - 1):
            for r in range(rows):
                current_col_sum += grid[r][c]                    
            if current_col_sum == target:
                return True

        return False 


#Minimum height roots
from collections import deque
 
def minHeightRoot(self, V, edges):
        if V <= 1:
            return [0]
            
        adj =[[] for _ in range(V)]
        degree = [0] * V
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        leaves = deque()
        for i in range(V):
            if degree[i] == 1:
                leaves.append(i)
                
        remaining_nodes = V
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
                        
        return sorted(list(leaves)) 