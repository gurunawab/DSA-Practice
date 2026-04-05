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