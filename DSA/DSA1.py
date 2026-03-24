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