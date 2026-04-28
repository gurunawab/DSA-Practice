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