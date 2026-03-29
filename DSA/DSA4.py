#Pythagorean Triplet
def pythagoreanTriplet(self, arr):
      
        s = set()
        max_val = 0
        for x in arr:
            s.add(x)
            max_val = max(max_val, x)
        
      
        nums = list(s)
        n = len(nums)
        
       
        for i in range(n):
            for j in range(i, n):
                a = nums[i]
                b = nums[j]
                
               
                sum_sq = a*a + b*b
                c = int(sum_sq**0.5)
                
              
                if c*c == sum_sq and c in s:
                    return True
                    
        return False 

#Find Unique Binary String
def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ans = []

        for i in range(len(nums)):
            curr_char = nums[i][i]

            if curr_char == "0":
                ans.append('1')
            else:
                ans.append('0')

        return "".join(ans)            
        

#Largest number in one swap
def largestSwap(self, s):
        num = list(s)
        
        last_index = {int(digit): i for i, digit in enumerate(s)}
        
        for i in range(len(num)):
            current_digit = int(num[i])
            
            for digit in range(9, current_digit, -1):
                if last_index.get(digit, -1) > i:
                    target_idx = last_index[digit]
                    num[i], num[target_idx] = num[target_idx], num[i]
                    
                    return "".join(num)
                    
        return s                


#Find All Possible Stable Binary Arrays 
def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                res0 = dp[i-1][j][0] + dp[i-1][j][1]

                if i > limit:
                    res0 -= dp[i-limit-1][j][1]

                dp[i][j][0] = res0 % MOD

                res1 = dp[i][j-1][0] + dp[i][j-1][1]

                if j > limit:
                    res1 -= dp[i][j-limit-1][0]

                dp[i][j][1] = res1 % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD       


#Articulation Point - II
import sys

# DFS recursion limit badhane ke liye
sys.setrecursionlimit(10**6)

class Solution:
    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        disc = [-1] * V
        low = [-1] * V
        is_ap = [False] * V
        self.timer = 0
        
        def dfs(u, p=-1):
            disc[u] = low[u] = self.timer
            self.timer += 1
            children = 0
            
            for v in adj[u]:
                if v == p: continue
                if disc[v] != -1:
                    # Back-edge update
                    low[u] = min(low[u], disc[v])
                else:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    # Articulation point condition
                    if p != -1 and low[v] >= disc[u]:
                        is_ap[u] = True
            
            # Special case for root
            if p == -1 and children > 1:
                is_ap[u] = True
        
        # Graph disconnected ho sakta hai isliye loop
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
        
        result = [i for i, val in enumerate(is_ap) if val]
        return sorted(result) if result else [-1]


#Find the String with LCP
def findTheString(self, lcp):
        n = len(lcp)
        ans = [""] * n
        char_code = ord('a')
        
   
        for i in range(n):
            if ans[i] == "":
              
                if char_code > ord('z'):
                    return ""
                
                curr_char = chr(char_code)
               
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        ans[j] = curr_char
                char_code += 1
        
        
        for s in ans:
            if s == "": return ""
            
        res = "".join(ans)
        
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                actual_lcp = 0
                if res[i] == res[j]:
                    if i + 1 < n and j + 1 < n:
                        actual_lcp = 1 + lcp[i+1][j+1]
                    else:
                        actual_lcp = 1
                
               
                if actual_lcp != lcp[i][j]:
                    return ""
                    
        return res                                          


#Partitions with Given Difference
def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        
        if (total_sum + diff) % 2 != 0 or total_sum < diff:
            return 0
            
        target = (total_sum + diff) // 2
        mod = 10**9 + 7
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % mod
                
        return dp[target]                              
