#Generate IP Addresses
class Solution:
    def generateIp(self, s):
        res = []
        
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start, dots, current_ip):
            if dots == 3:
                last_part = s[start:]
                
                if self.is_valid(last_part):
                    res.append(current_ip + last_part)
                return
            
            for length in range(1, 4):
                if start + length < len(s):
                    part = s[start:start + length]
                    if self.is_valid(part):
                        backtrack(start + length, dots + 1, current_ip + part + ".")
                        
        backtrack(0, 0, "")
        return res
        
    def is_valid(self, segment):
        if not segment or len(segment) > 3:
            return False
            
        if segment[0] =='0' and len(segment) > 1:
            return False
            
        return 0 <= int(segment) <= 255    
    

#Minimum Number of Seconds to Make Mountain Height Zero
import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_reduce(time_limit):
            total_reduction = 0
            for w_time in workerTimes:
           
                val = (2 * time_limit) // w_time
                x = int((-1 + math.sqrt(1 + 4 * val)) // 2)
                
                total_reduction += x
                if total_reduction >= mountainHeight:
                    return True
            return total_reduction >= mountainHeight

        low = 0
       
        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans


#top view of binary tree
from collections import deque


def topView(self, root):
        if not root:
            return []
            
        hd_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            curr_node, hd = queue.popleft()
            
            if hd not in hd_map:
                hd_map[hd] = curr_node.data
                
            if curr_node.left:
                queue.append((curr_node.left, hd - 1))
                
            if curr_node.right:
                queue.append((curr_node.right, hd + 1))
                
        result = [hd_map[hd] for hd in sorted(hd_map.keys())]
        
        return result 


#The k-th Lexicographical String of All Happy Strings of Length n
def getHappyString(self, n, k):
        
        result = []

        def backtrack(current_string):
            if len(current_string) == n:
                result.append(current_string)
                return

            for char in ['a', 'b', 'c']:
                if len(current_string) == 0 or current_string[-1] != char:
                    backtrack(current_string + char)

                    if len(result) == k:
                        return 

        backtrack("")

        if len(result) < k:
            return ""
        else:
            return result[k-1] 


#Distribute Candies
def distCandy(self, root):
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
                
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            self.moves += abs(left_balance) + abs(right_balance)
            
            return (node.data + left_balance + right_balance) - 1
            
        dfs(root)
        return self.moves


#Count Submatrices with Top-Left Element and Sum Less Than k
def countSubmatrices(self, grid, k):
        
        m = len(grid)
        n = len(grid[0])
        count = 0

        pref = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                current_val = grid[r][c]

                above = pref[r-1][c] if r > 0 else 0

                left = pref[r][c-1] if c > 0 else 0

                diagonal = pref[r-1][c-1] if (r > 0 and c > 0) else 0

                pref[r][c] = current_val + above + left - diagonal

                if pref[r][c] <= k:
                    count += 1
                else:
                    break

        return count  


#Predecessor and Successo
def findPreSuc(self, root, key):
        pre = None
        suc = None
        curr = root
        
        while curr:
            
            if curr.data == key:
                
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    pre = temp
                    
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                break
            
            elif curr.data > key:
                suc = curr
                curr = curr.left
                
            else:
                pre = curr
                curr = curr.right
                
        return pre, suc  



#Length of Longest Cycle in a Graph
def longestCycle(self, V, edges):
        adj = [-1] * V
        for u, v in edges:
            adj[u] = v
            
        visited = [False] * V
        max_cycle = -1
        
        for i in range(V):
            if visited[i]:
                continue
            
            curr_path_dist = {}
            curr = i
            distance = 0
            
            while curr != -1 and not visited[curr]:
                visited[curr] = True
                curr_path_dist[curr] = distance
                distance += 1
                curr = adj[curr]
                
            if curr != -1 and curr in curr_path_dist:
                cycle_len = distance - curr_path_dist[curr]
                max_cycle = max(max_cycle, cycle_len)
                
        return max_cycle        
        

#Maximum Non Negative Product in a Matrix
def maxProductPath(self, grid):
        
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]

        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                vals = (
                    max_dp[i-1][j] * grid[i][j],
                    min_dp[i-1][j] * grid[i][j],
                    max_dp[i][j-1] * grid[i][j],
                    min_dp[i][j-1] * grid[i][j]
                )
                max_dp[i][j] = max(vals)
                min_dp[i][j] = min(vals)

        res = max_dp[-1][-1]

        return res % MOD if res >= 0 else -1  

#Sorted subsequence of size 3
def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

         
        smaller = [-1] * n
        min_idx = 0
        for i in range(1, n):
            if arr[i] <= arr[min_idx]:
                min_idx = i
                smaller[i] = -1
            else:
                smaller[i] = min_idx

       
        greater = [-1] * n
        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_idx]:
                max_idx = i
                greater[i] = -1
            else:
                greater[i] = max_idx

       
        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]

        
        return []

#Minimum Initial Energy to Finish Tasks
def minimumEffort(self, tasks):
        
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        initial_energy = 0
        current_energy = 0

        for actual, minimum in tasks:

            if current_energy < minimum:

                needed = minimum - current_energy
                initial_energy += needed
                current_energy += needed

            current_energy -= actual

        return initial_energy 
