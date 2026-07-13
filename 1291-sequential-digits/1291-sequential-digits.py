class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        digits = "123456789"
        
       
        min_len = len(str(low))
        max_len = len(str(high))
        
       
        for length in range(min_len, max_len + 1):
          
            for i in range(10 - length):
                substring = digits[i:i + length]
                num = int(substring)
                
              
                if low <= num <= high:
                    result.append(num)
                    
        return result
        