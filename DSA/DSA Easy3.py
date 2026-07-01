#Maximum Area Between Bars
def maxArea(self, height):
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if height[i] <= height[j]:
                h = height[i]
                i += 1
            else:
                h = height[j]
                j -= 1
            max_area = max(max_area, (j - i) * h)
        return max_area

#Maximum Number of People Defeated
def maxPeopleDefeated(self, p: int) -> int:
        n = 0
        total_strength_needed = 0
        
        while True:
            n += 1
            
            next_person_strength = n * n
            
            
            if total_strength_needed + next_person_strength <= p:
                total_strength_needed += next_person_strength
            else:
                
                return n - 1

#N-Digit Numbers with Increasing Digits
def increasingNumbers(self, n):
        
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
       
        if n > 9:
            return []
            
        result = []
        
        def backtrack(current_num, last_digit):
            
            if len(current_num) == n:
                result.append(int(current_num))
                return
            
            
            for next_digit in range(last_digit + 1, 10):
                backtrack(current_num + str(next_digit), next_digit)
        
       
        for start_digit in range(1, 10):
            backtrack(str(start_digit), start_digit)
            
        return result

#Ways to Tile the Floor
def countWays(self, n, m):
        MOD = 10**9 + 7
        
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if i < m:
                
                dp[i] = 1
            elif i == m:
              
                dp[i] = 2
            else:
                
                dp[i] = (dp[i - 1] + dp[i - m]) % MOD
                
        return dp[n]

#Count Matching Subsequences
def countWays(self, s1, s2):
        n = len(s1)
        m = len(s2)
        MOD = 10**9 + 7
        
     
        dp = [0] * (m + 1)
        
        
        dp[0] = 1
        
        for i in range(1, n + 1):
           
            for j in range(m, 0, -1):
                if s1[i-1] == s2[j-1]:
                    dp[j] = (dp[j] + dp[j-1]) % MOD
        
        return dp[m]

#k Times Appearing Adjacent Two 1's
def countStrings(self, n, k):
        MOD = 10**9 + 7
        
        
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
        
        
        dp[1][0][0] = 1 
        dp[1][0][1] = 1 
        
        for i in range(2, n + 1):
            for j in range(k + 1):
               
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                
               
                dp[i][j][1] = dp[i-1][j][0]
              
                if j > 0:
                    dp[i][j][1] = (dp[i][j][1] + dp[i-1][j-1][1]) % MOD
                    
        return (dp[n][k][0] + dp[n][k][1]) % MOD

#Maximum Element After Decreasing and Rearranging
def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    
        arr.sort()
        
     
        arr[0] = 1
        
       
        for i in range(1, len(arr)):
           
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        
        
        return arr[-1]  

#Max Dot Product with 0 Insertions
def maxDotProduct(self, arr, brr):
        m = len(brr)
        dp = [0] * (m + 1)
        for i, a in enumerate(arr):
            for j in reversed(range(min(i + 1, m))):
                dp[j + 1] = max(dp[j + 1], dp[j] + a * brr[j])
        return dp[m]

#Minimum Insert and Delete to Convert
from bisect import bisect_left

class Solution:
    def minInsAndDel(self, a, b):
       
        b_set = set(b)
        
        
        filtered_a = [x for x in a if x in b_set]
        
        
        lis = []
        for x in filtered_a:
            idx = bisect_left(lis, x)
            if idx < len(lis):
                lis[idx] = x
            else:
                lis.append(x)
        
        lcs_length = len(lis)
        
      
        return (len(a) - lcs_length) + (len(b) - lcs_length)   

#Max Subarray Sum by Removing At Most One
def maxSumSubarray(self, arr):
        n = len(arr)
        if n == 0: return 0
        if n == 1: return arr[0]
        
        
        forward = [0] * n
        forward[0] = arr[0]
        max_so_far = arr[0]
        for i in range(1, n):
            forward[i] = max(arr[i], forward[i-1] + arr[i])
            max_so_far = max(max_so_far, forward[i])
            
       
        backward = [0] * n
        backward[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            backward[i] = max(arr[i], backward[i+1] + arr[i])
            
        
        for i in range(1, n - 1):
            max_so_far = max(max_so_far, forward[i-1] + backward[i+1])
            
        return max_so_far                               