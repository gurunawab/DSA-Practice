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
