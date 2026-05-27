#Last Coin in a Game of Alternates
def coin(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            if arr[left] >= arr[right]:
                left += 1
            else:
                right -= 1
                
        return arr[left] 

#Wifi Range
def wifiRange(self, s: str, x: int) -> bool:
       
        if '1' not in s:
            return False
            
        
        segments = s.split('1')
        
        
        if len(segments[0]) > x:
            return False
            
        
        if len(segments[-1]) > x:
            return False
            
        
        for i in range(1, len(segments) - 1):
            if len(segments[i]) > 2 * x:
                return False
                
        return True        