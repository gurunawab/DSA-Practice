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