#Common in 3 Sorted Arrays
def commonElements(self, a, b, c):
        common = set(a) & set(b) & set(c)
        
        return sorted(list(common))

#Smallest window containing 0, 1 and 2
def smallestSubstring(self, s):
        pos = {'0':-1, '1':-1, '2':-1}
        min_len = float('inf')
        
        for i, char in enumerate(s):
            pos[char] = i
            
            if -1 not in pos.values():
                min_len = min(min_len, i - min(pos.values()) + 1)
                
        return min_len if min_len != float('inf') else -1        

# Minimum Operations to Make a Uni-Value Grid
def minOperations(self, grid, x):
        nums = sorted([val for row in grid for val in row])

        if any((n - nums[0]) % x != 0 for n in nums):
            return -1

        median = nums[len(nums) // 2]

        return sum(abs(n - median) // x for n in nums)  

#Min Swaps to Group 1s
def minSwaps(self, arr):
        n = len(arr)
        k = sum(arr)
        
        if k == 0: return -1
        
        curr_ones = sum(arr[:k])
        max_ones = curr_ones
        
        for i in range(k, n):
            curr_ones += arr[i] - arr[i-k]
            max_ones = max(max_ones, curr_ones)
            
        return k - max_ones

#Check if an Array is Max Heap
def isMaxHeap(self, arr):
        n = len(arr)
        
        for i in range(n // 2):
            if (2 * i + 1 < n) and (arr[i] < arr[2 * i + 1]):
                return False
                
            if (2 * i + 2 < n) and (arr[i] < arr[2 * i + 2]):
                return False
                
        return True        

#Rotate Function
def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)

        f = sum(i * v for i, v in enumerate(nums))

        max_f = f

        for i in range(1, n):
            f = f + total_sum - n * nums[n - i]
            if f > max_f:
                max_f = f

        return max_f                         