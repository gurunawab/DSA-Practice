#Maximum Twin Sum of a Linked List
def pairSum(self, head):
        
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
       
        
        
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        
        
        
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            current_twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_twin_sum)
            
           
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum

#Exit Point in a Matrix
def exitPoint(self, mat: list[list[int]]) -> list[int]:
        
        n = len(mat)
        m = len(mat[0])
        
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
       
        i, j = 0, 0
        dir_idx = 0
        
        
        last_i, last_j = 0, 0
        
        while 0 <= i < n and 0 <= j < m:
           
            last_i, last_j = i, j
            
            
            if mat[i][j] == 1:
                mat[i][j] = 0
                dir_idx = (dir_idx + 1) % 4
            
           
            i += directions[dir_idx][0]
            j += directions[dir_idx][1]
            
        return [last_i, last_j]

#Process String with Special Operations II
def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        curr_len = 0

        for i in range(n):
            ch = s[i]
            if ch.islower():
                curr_len += 1
            elif ch == '*':
                curr_len = max(0, curr_len - 1)
            elif ch == '#':
                curr_len *= 2
            elif ch == '%':
                pass

            lengths[i] = curr_len

        if k >= curr_len or curr_len == 0:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i-1] if i > 0 else 0

            if ch.islower():

                if k == lengths[i] - 1:
                    return ch

            elif ch == '#':

                if k >= prev_len:
                    k -= prev_len

            elif ch == '%':

                k = lengths[i] - 1 - k

            elif ch == '*':

                pass

        return "." 

#Coverage of all Zeros in a Binary Matrix
def findCoverage(self, mat):
        
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0
        
        total_coverage = 0
        
        
        for i in range(n):
            for j in range(m):
                
                if mat[i][j] == 0:
                    
                   
                    for k in range(j - 1, -1, -1):
                        if mat[i][k] == 1:
                            total_coverage += 1
                            break
                            
                    
                    for k in range(j + 1, m):
                        if mat[i][k] == 1:
                            total_coverage += 1
                            break
                            
                    
                    for k in range(i - 1, -1, -1):
                        if mat[k][j] == 1:
                            total_coverage += 1
                            break
                            
                    
                    for k in range(i + 1, n):
                        if mat[k][j] == 1:
                            total_coverage += 1
                            break
                            
        return total_coverage           

#Maximum Ice Cream Bars
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
       
        max_cost = max(costs)
        
       
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
            
        ice_cream_count = 0
        
      
        for cost in range(1, max_cost + 1):
            if freq[cost] > 0:
                
                count_to_buy = min(freq[cost], coins // cost)
                
               
                if count_to_buy == 0:
                    break
                    
               
                ice_cream_count += count_to_buy
                coins -= count_to_buy * cost
                
        return ice_cream_count 
        
#Number of ZigZag Arrays II
class Solution:
    MOD = 10**9 + 7

    def multiply(self, A, B):
        sz = len(A)
        C = [[0] * sz for _ in range(sz)]

        for i in range(sz):
            for k in range(sz):
                if A[i][k] == 0:
                    continue
                for j in range(sz):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % self.MOD

        return C

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:
            return r - l + 1

        k = r - l + 1
        sz = 2 * k

        M = [[0] * sz for _ in range(sz)]

        for i in range(k):
            for j in range(i):
                M[i][k + j] = 1

            for j in range(i + 1, k):
                M[k + i][j] = 1

        res = [[0] * sz for _ in range(sz)]

        for i in range(sz):
            res[i][i] = 1

        p = n - 1

        while p > 0:
            if p % 2 == 1:
                res = self.multiply(res, M)

            M = self.multiply(M, M)
            p //= 2

        ans = 0

        for i in range(sz):
            for j in range(sz):
                ans = (ans + res[i][j]) % self.MOD

        return ans                                