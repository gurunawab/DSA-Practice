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
        