#Get Biggest Three Rhombus Sums in a Grid
def getBiggestThree(self, grid):
       
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
        

#Number of BST From Array
def countBSTs(self, arr):
        n = len(arr)
        if n == 0:
            return []
            
        def get_catalan(limit):
            catalan = [0] * (limit + 1)
            catalan[0] = 1
            for i in range(1, limit + 1):
                catalan[i] = (catalan[i-1] * (4*i - 2)) // (i + 1)
            return catalan
            
        catalan_table = get_catalan(n)
        
        sorted_arr = sorted(arr)
        
        val_to_idx = {val: i for i, val in enumerate(sorted_arr)}
        
        ans = []
        
        for x in arr:
            idx = val_to_idx[x]
            left_nodes = idx
            right_nodes = n - 1 - idx
            
            count = catalan_table[left_nodes] * catalan_table[right_nodes]
            ans.append(count)
            
        return ans    


#Stable Marriage Problem
def stableMarriage(self, men, women):
        n = len(men)
        
        women_ranks = [[0] * n for _ in range(n)]
        for i in range(n):
            for rank, man_idx in enumerate(women[i]):
                women_ranks[i][man_idx] = rank
                
        women_partner = [-1] * n
        man_partner = [-1] * n
        
        free_men = list(range(n))
        
        next_proposal_index = [0] * n
        
        while free_men:
            m = free_men.pop(0)
            
            w = men[m][next_proposal_index[m]]
            next_proposal_index[m] += 1
            
            if women_partner[w] == -1:
                women_partner[w] = m
                man_partner[m] = w
            else:
                current_m = women_partner[w]
                
                if women_ranks[w][m] < women_ranks[w][current_m]:
                    free_men.append(current_m)
                    women_partner[w] = m
                    man_partner[m] = w
                else:
                    free_men.append(m)
                    
        return man_partner 