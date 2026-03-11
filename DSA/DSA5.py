#Subarrays with First Element Minimum
def countSubarrays(self, arr):
        n = len(arr)
        
        nse = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                nse[index] = i
            stack.append(i)
            
        ans = 0
        
        for i in range(n):
            ans += (nse[i] - i)
            
        return ans 


#Sum of subarray minimums
def sumSubMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        stack = []    
            
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        total_sum = 0
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            total_sum += count * arr[i]
            
        return total_sum    
        