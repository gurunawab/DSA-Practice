#Generate IP Addresses
class Solution:
    def generateIp(self, s):
        res = []
        
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start, dots, current_ip):
            if dots == 3:
                last_part = s[start:]
                
                if self.is_valid(last_part):
                    res.append(current_ip + last_part)
                return
            
            for length in range(1, 4):
                if start + length < len(s):
                    part = s[start:start + length]
                    if self.is_valid(part):
                        backtrack(start + length, dots + 1, current_ip + part + ".")
                        
        backtrack(0, 0, "")
        return res
        
    def is_valid(self, segment):
        if not segment or len(segment) > 3:
            return False
            
        if segment[0] =='0' and len(segment) > 1:
            return False
            
        return 0 <= int(segment) <= 255    
    

#Minimum Number of Seconds to Make Mountain Height Zero
import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_reduce(time_limit):
            total_reduction = 0
            for w_time in workerTimes:
           
                val = (2 * time_limit) // w_time
                x = int((-1 + math.sqrt(1 + 4 * val)) // 2)
                
                total_reduction += x
                if total_reduction >= mountainHeight:
                    return True
            return total_reduction >= mountainHeight

        low = 0
       
        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans