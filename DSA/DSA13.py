#Count Subarrays With Majority Element I
from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        arr = [1 if x == target else -1 for x in nums]
        
     
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + arr[i]
            
        
        def count_smaller(arr):
            sorted_arr = sorted(list(set(arr)))
            rank = {val: i + 1 for i, val in enumerate(sorted_arr)}
            
            bit = [0] * (len(sorted_arr) + 1)
            def update(i, delta):
                while i < len(bit):
                    bit[i] += delta
                    i += i & (-i)
            def query(i):
                s = 0
                while i > 0:
                    s += bit[i]
                    i -= i & (-i)
                return s
            
            count = 0
            for x in arr:
                count += query(rank[x] - 1)
                update(rank[x], 1)
            return count

        return count_smaller(prefix_sums)

#Find the Maximum Number of Elements in Subset
from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counts = Counter(nums)
        ans = 1
        
       
        if 1 in counts:
            if counts[1] % 2 == 0:
                ans = counts[1] - 1
            else:
                ans = counts[1]
                
      
        for x in counts:
            if x == 1: continue
            
            curr = x
            length = 0
           
            while counts[curr] >= 2:
                length += 2
                curr *= curr
            
           
            if counts[curr] >= 1:
                length += 1
            else:
                
                length -= 1
                
            ans = max(ans, length)
            
        return ans