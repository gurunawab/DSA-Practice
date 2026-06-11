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

#Substring with Max Zero-One Diff
def maxSubstring(self, s: str) -> int:
        max_so_far = float('-inf')
        current_max = 0
        
        for char in s:
          
            val = 1 if char == '0' else -1
            
            current_max += val
            
           
            if current_max > max_so_far:
                max_so_far = max_so_far = current_max
            
          
            if current_max < 0:
                current_max = 0
                
        return max_so_far  

#Left and Right Sum Differences
def leftRightDifference(self, nums):
        
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            
            right_sum -= num
            
            
            answer.append(abs(left_sum - right_sum))
            
            
            left_sum += num
            
        return answer      

#Finding Profession
def profession(self, level, pos):
        
        set_bits_count = bin(pos - 1).count('1')
        
        
        if set_bits_count % 2 != 0:
            return 'Doctor'
        else:
            return 'Engineer'

#Partition Array According to Given Pivot
def pivotArray(self, nums, pivot):
        
        less = []
        equal = []
        greater = []
        
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
                
        
        return less + equal + greater  

#Binary Searchable Count
def binarySearchable(self, arr):
        c = 0
        n = len(arr)

        for i in range(n):
            x = arr[i]
            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2

                if x == arr[mid]:
                    c += 1
                    break

                if arr[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1

        return c

#Equal Point in Brackets
def findIndex(self, s: str) -> int:
        n = len(s)
        
        count_close = s.count(')')
        count_open = 0
        
        for i in range(n):
            
            if count_open == count_close:
                return i
            
            if s[i] == '(':
                count_open += 1
            elif s[i] == ')':
                count_close -= 1
                
        if count_open == count_close:
            return n 
            
        return -1           