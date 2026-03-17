#Get Biggest Three Rhombus Sums in a Grid
def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])
        sums = set()

        for r in range(rows):
            for c in range(cols):
                sums.add(grid[r][c])

                s = 1

                while r + 2 * s < rows and c - s >= 0 and c + s < cols:
                    current_sum = 0

                    for i in range(s):
                        current_sum += grid[r + i][c + i]

                    for i in range(s):
                        current_sum += grid[r + s + i][c + s - i]

                    for i in range(s):
                        current_sum += grid[r + 2 * s - i][c - i]

                    for i in range(s):
                        current_sum += grid[r + s - i][c - s + i]

                    sums.add(current_sum)
                    s += 1

        res = sorted(list(sums), reverse=True)

        return res[:3]                            
        

#K Sum Paths
def countAllPaths(self, root, k):
        prefix_sums = {0: 1}
        
        def solve(node, current_sum):
            if not node:
                return 0
                
            current_sum += node.data
            
            count = prefix_sums.get(current_sum - k, 0)
            
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            count += solve(node.left, current_sum)
            count += solve(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
            
            return count
            
        return solve(root, 0)    


#Vertical Tree Traversal
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
            
        hd_map = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            if node:
                hd_map[hd].append(node.data)
                
                if node.left:
                    queue.append((node.left, hd - 1))
                if node.right:
                    queue.append((node.right, hd + 1))
        
        result = []
        for hd in sorted(hd_map.keys()):
            result.append(hd_map[hd])
            
        return result    
        

#Fancy Sequence
def __init__(self):
        self.nums = []
        self.a = 1
        self.b = 0
        self.MOD = 10**9 + 7

def append(self, val):
        
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        self.nums.append(((val - self.b) * inv_a) % self.MOD)

def addAll(self, inc):
        self.b = (self.b + inc) % self.MOD

def multAll(self, m):
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

def getIndex(self, idx):
        if idx >= len(self.nums):
            return -1
        
        return (self.nums[idx] * self.a + self.b) % self.MOD 


#Burning Tree
def minTime(self, root, target):
        parent_map = {}
        target_node = None
        
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.data == target:
                target_node = curr
                
            if curr.left:
                parent_map[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent_map[curr.right] = curr
                queue.append(curr.right)
                
        q = deque([target_node])
        visited = {target_node}
        time = 0
        
        while q:
            level_size = len(q)
            flame_spread = False
            
            for _ in range(level_size):
                curr = q.popleft()
                
                for neighbor in [curr.left, curr.right, parent_map.get(curr)]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        flame_spread = True
                        
            if flame_spread:
                time += 1
                
        return time        


#Largest Submatrix With Rearrangements
def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i-1][j]

            curr_row = sorted(matrix[i], reverse=True)

            for j in range(n):
                height = curr_row[j]
                width = j + 1
                ans = max(ans, height * width)

        return ans                
        