class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = cur_sum = max_len = 0
        for right, val in enumerate(nums):
            cur_sum += val
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len > 0 else -1