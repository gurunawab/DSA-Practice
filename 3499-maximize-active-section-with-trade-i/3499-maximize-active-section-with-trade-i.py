class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        t = '1' + s + '1'
        
     
        L = []
        Z = []
        
        i = 0
        n = len(t)
        while i < n:
           
            count1 = 0
            while i < n and t[i] == '1':
                count1 += 1
                i += 1
            L.append(count1)
            
            if i >= n:
                break
                
          
            count0 = 0
            while i < n and t[i] == '0':
                count0 += 1
                i += 1
            Z.append(count0)
            
        initial_ones = s.count('1')
        
        
        if len(L) <= 2:
            return initial_ones
            
       
        max_gain = 0
        for i in range(1, len(L) - 1):
            gain = Z[i - 1] + Z[i]
            if gain > max_gain:
                max_gain = gain
                
        return initial_ones + max_gain