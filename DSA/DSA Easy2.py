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

#Vertical Sum
def verticalSum(self, root):
        hd_sums = {}
        
        def traverse(node, hd):
            if not node:
                return
            
            hd_sums[hd] = hd_sums.get(hd, 0) + node.data
            
            traverse(node.left, hd - 1)
            traverse(node.right, hd + 1)
            
        traverse(root, 0)
        
        return [hd_sums[hd] for hd in sorted(hd_sums.keys())]      

#Minimum Element After Replacement With Digit Sum
def minElement(self, nums):
       
        min_sum = float('inf') 
        
        for num in nums:
            current_sum = 0
          
            while num > 0:
                current_sum += num % 10
                num //= 10
            
           
            if current_sum < min_sum:
                min_sum = current_sum
                
        return min_sum