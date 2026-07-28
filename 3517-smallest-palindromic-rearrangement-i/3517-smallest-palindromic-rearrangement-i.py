class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        half_len = n // 2
        
        
        left_half = "".join(sorted(s[:half_len]))
        
       
        right_half = left_half[::-1]
        
        
        if n % 2 != 0:
            mid_char = s[half_len]
            return left_half + mid_char + right_half
        else:
            return left_half + right_half
        