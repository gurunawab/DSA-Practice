class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pos = {v: i for i, v in enumerate(sorted(nums, key=lambda x: (sum(map(int, str(x))), x)))}
        vis, swaps = [False] * len(nums), 0
        for i in range(len(nums)):
            while not vis[i]:
                vis[i] = True
                i = pos[nums[i]]
                swaps += not vis[i]
        return swaps
