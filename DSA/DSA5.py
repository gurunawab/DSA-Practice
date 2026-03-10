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