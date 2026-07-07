class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
     
        s = str(n)
        
        
        non_zero_chars = [char for char in s if char != '0']
        
       
        if not non_zero_chars:
            return 0
        
       
        x = int("".join(non_zero_chars))
        
      
        digit_sum = sum(int(digit) for digit in str(x))
        
       
        return x * digit_sum