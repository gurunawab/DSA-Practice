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


#Chocolates Pickup


#Number of Ways to Arrive at Destination
def countPaths(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        dist = [float('inf')] * V
        ways = [0] * V
        mod = 10**9 + 7
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, weight in adj[u]:
                
                if d + weight < dist[v]:
                    dist[v] = d + weight
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                    
                elif d + weight == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % mod
                    
        return ways[V-1]

#Minimum Distance to Type a Word Using Two Fingers
def minimumDistance(self, word):
       
        def get_dist(char1, char2):
            if char1 is None: return 0
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            r1, col1 = divmod(c1, 6)
            r2, col2 = divmod(c2, 6)
            return abs(r1 - r2) + abs(col1 - col2)

        memo = {}

        def solve(idx, f2):
            if idx == len(word):
                return 0

            state = (idx, f2)
            if state in memo:
                return memo[state]

            f1 = word[idx - 1]
            curr_char = word[idx]

            dist1 = get_dist(f1, curr_char) + solve(idx + 1, f2)
            dist2 = get_dist(f2, curr_char) + solve(idx + 1, f1)

            res = min(dist1, dist2)
            memo[state] = res
            return res

        return solve(1, None) 

#Minimize Hamming Distance After Swap Operations
from collections import defaultdict, Counter

def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        for a, b in allowedSwaps:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        res = 0
        for indices in groups.values():
            count = Counter(source[i] for i in indices)

            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1
        return res    

#TwoWater jug Problems
def minSteps(self, m, n, d):
        if d > max(m, n) or d % math.gcd(m, n) != 0:
            return -1
            
        def solve(from_cap, to_cap, target):
            from_jug, to_jug = from_cap, 0
            steps = 1
            
            while from_jug != target and to_jug != target:
                temp = min(from_jug, to_cap - to_jug)
                
                to_jug += temp
                from_jug -= temp
                steps += 1
                
                if from_jug == target or to_jug == target:
                    break
                
                if from_jug == 0:
                    from_jug = from_cap
                    steps += 1
                elif to_jug == to_cap:
                    to_jug = 0
                    steps += 1
                    
            return steps
            
        return min(solve(m, n, d), solve(n, m, d))   