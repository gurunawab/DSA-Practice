#Print Diagonally
def diagView(self, mat): 
        n =len(mat)
        result = []
        
        for s in range(2 * n - 1):
            start_i = max(0, s - (n - 1))
            
            end_i = min(s, n -1)
            
            for i in range(start_i, end_i + 1):
                j = s - i
                result.append(mat[i][j])
                
        return result 


#Painting the Fence
def countWays(self,n,k):
        if n == 1:
            return k
            
        same = k
        diff = k * (k - 1)
        total = same + diff
        
        for i in range(3, n + 1):
            same = diff
            diff = total * (k - 1)
            total = same + diff
            
        return total  

  
#Robot Return to Origin
def judgeCircle(self, moves):
       
        x = 0
        y = 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1

        return x == 0 and y == 0   


#Target Sum
def totalWays(self, arr, target):
        total_sum = sum(arr)
        
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
            
        subset_sum = (target + total_sum) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]        

#Gray Code
def graycode(self,n):
        if n <= 0:
            return ["0"]
        if n == 1:
            return ["0", "1"]
            
        previous_gray = self.graycode(n - 1)
        
        res = ["0" + s for s in previous_gray]
        
        reversed_gray = previous_gray[::-1]
        res.extend(["1" + s for s in reversed_gray])
        
        return res


#Segregate 0s and 1s
def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            while left < right and arr[left] == 0:
                left += 1
                
            while left < right and arr[right] == 1:
                right -= 1
                
            if left < right:
                arr[left] = 0
                arr[right] = 1
                left += 1
                right -= 1

#XOR After Range Multiplication Queries I
def xorAfterQueries(self, nums, queries):
        
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        result = 0
        for num in nums:
            result ^= num

        return result     

#Intersection of Two Sorted Arrays
def intersection(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []
        
        while i < n and j < m:
           
            if a[i] < b[j]:
                i += 1
            
            elif b[j] < a[i]:
                j += 1
            
            else:
              
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
                
        return result   


#Minimum Distance Between Three Equal Elements I
import collections

class Solution(object):
    def minimumDistance(self, nums):
       
        index_map = collections.defaultdict(list)
        for idx, val in enumerate(nums):
            index_map[val].append(idx)

        min_dist = float('inf')
        found = False

        for val in index_map:
            indices = index_map[val]

            if len(indices) >= 3:

                for i in range(len(indices) - 2):
                    current_dist = 2 * (indices[i+2] - indices[i])

                    min_dist = min(min_dist, current_dist)

                    found = True

        return min_dist if found else -1  

#Count increasing Subarrays
def countIncreasing(self, arr):
        n = len(arr)
        if n < 2:
            return 0
            
        total_count = 0
        current_len = 1
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                total_count += current_len
                current_len += 1
            else:
                current_len = 1
                
        return total_count  

#Toeplitz matrix
def isToeplitz(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows - 1):
            for j in range(cols - 1):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False
                    
        return True 

#Minimum Distance to the Target Element
def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        
       
        for i, num in enumerate(nums):
            if num == target:
               
                min_dist = min(min_dist, abs(i - start))
                
        return min_dist      

#URLify a given string
def URLify(self, s): 
        return s.replace(' ', '%20')

#Shortest Distance to Target String in a Circular Array
def closestTarget(self, words, target, startIndex):
        
        n = len(words)
        min_dist = n
        found = False

        for i in range(n):
            if words[i] == target:
                found = True

                abs_diff = abs(i - startIndex)

                current_dist = min(abs_diff, n - abs_diff)

                min_dist = min(min_dist, current_dist)

        return min_dist if found else -1 

#Implement Atoi
def myAtoi(self, s:str) -> int:
        s = s.lstrip()
        if not s:return 0
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']: s = s[1:]
        
        res = 0
        for char in s:
            if not char.isdigit(): break
            res = res * 10 + int(char)
            
        res = max(-2**31, min(sign * res, 2**31 - 1))
        return res