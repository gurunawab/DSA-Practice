#Lexicographically smallest after removing k
def lexicographicallySmallest(self, s: str, k: int) -> str:
        n = len(s)
        
        
        is_power_of_2 = (n > 0) and (n & (n - 1)) == 0
        
        
        if is_power_of_2:
            k = k // 2
        else:
            k = k * 2
            
        
        if k >= n or n == 0:
            return "-1"
            
        
        stack = []
        removals_left = k
        
        for char in s:
            
            while stack and removals_left > 0 and stack[-1] > char:
                stack.pop()
                removals_left -= 1
            stack.append(char)
            
        
        if removals_left > 0:
            stack = stack[:-removals_left]
            
        return "".join(stack)

#Non-Attacking Black and White Knights
def numOfWays(self, n: int, m: int) -> int:
       
        total_squares = n * m
        
        
        total_ways = total_squares * (total_squares - 1)
        
       
        attacking_2x3 = 0
        if n >= 2 and m >= 3:
            attacking_2x3 = (n - 1) * (m - 2)
            
        
        attacking_3x2 = 0
        if n >= 3 and m >= 2:
            attacking_3x2 = (n - 2) * (m - 1)
            
       
        total_attacking_ways = 4 * (attacking_2x3 + attacking_3x2)
        
        
        return total_ways - total_attacking_ways


 
#Create Binary Tree From Descriptions
def createBinaryTree(self, descriptions):
        
        nodes = {}
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]
            
            
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]
            
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            
            children.add(child_val)
            
        
        for parent_val in nodes:
            if parent_val not in children:
                return nodes[parent_val]  


#Maximum Total Subarray Value II
class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        LUT = SparseTable(nums)

        pq = [(-LUT.query(i, n), i, n) for i in range(n)]

        res = 0
        for _ in range(k):
            val, l, r = pq[0]
            if val == 0:
                break
            res -= val
            heapq.heapreplace(pq, (-LUT.query(l, r - 1), l, r - 1))

        return res

class SparseTable:
    def __init__(self, num: list[int]):
        n = len(num)
        bitWidth = n.bit_length()
        self.Min = [[0] * n for _ in range(bitWidth)]
        self.Max = [[0] * n for _ in range(bitWidth)]

        for i in range(n):
            self.Min[0][i] = self.Max[0][i] = num[i]

        for i in range(1, bitWidth):
            for j in range(n - (1 << i) + 1):
                self.Min[i][j] = min(self.Min[i - 1][j], self.Min[i - 1][j + (1 << (i - 1))])
                self.Max[i][j] = max(self.Max[i - 1][j], self.Max[i - 1][j + (1 << (i - 1))])

    def query(self, left: int, right: int) -> int:
        k = (right - left).bit_length() - 1
        return max(self.Max[k][left], self.Max[k][right - (1 << k)]) - \
               min(self.Min[k][left], self.Min[k][right - (1 << k)])  

#Number of Ways to Assign Edge Weights I
from collections import defaultdict, deque

class Solution(object):
    def assignEdgeWeights(self, edges):
        
        if not edges:
            return 0
        
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        max_depth = 0
   
        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
       
        MOD = 10**9 + 7
        
        
        if max_depth == 0:
            return 0
            
        return pow(2, max_depth - 1, MOD)  


#Number of Ways to Assign Edge Weights II
import sys


sys.setrecursionlimit(200000)

class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        MOD = 10**9 + 7
        
       
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        
        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
                    
        
        dfs(1, 1, 0)
        
        
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
            
        
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
                
            lca = get_lca(u, v)
            path_length = depth[u] + depth[v] - 2 * depth[lca]
            
            
            ans = pow2[path_length - 1]
            answer.append(ans)
            
        return answer 

#Check Repeated Substring with K Replacements
from collections import Counter

class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n % k != 0:
            return False
            
        chunks = [s[i:i+k] for i in range(0, n, k)]
        
        chunk_counts = Counter(chunks)
        
        if len(chunk_counts) == 1:
            return True
            
        if len(chunk_counts) == 2:
            
            if 1 in chunk_counts.values():
                return True
                
        return False 


#Binary Strings with Equal Sum of Two Halves
def computeValue(self, n: int) -> int:
        MOD = 10**9 + 7
        
        limit = 2 * n
        
        fact = [1] * (limit + 1)
        for i in range(1, limit + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
            
        numerator = fact[2 * n]
        
        denominator = (fact[n] * fact[n]) % MOD
        
        denominator_inv = pow(denominator, MOD - 2, MOD)
        
        return (numerator * denominator_inv) % MOD

