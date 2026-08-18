from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        freq = Counter()
        
        for i in range(len(nums) - k + 1):
            for x in set(nums[i : i + k]):
                freq[x] += 1
                
        valid = [x for x, count in freq.items() if count == 1]
        return max(valid) if valid else -1