class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result = []
        curr = 1  
        
        for num in target:
            
            while curr < num:
                result.append("Push")
                result.append("Pop")
                curr += 1
            
            
            result.append("Push")
            curr += 1
            
        return result