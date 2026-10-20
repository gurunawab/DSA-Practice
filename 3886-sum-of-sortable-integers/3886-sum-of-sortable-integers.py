class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def check(k: int) -> bool:
            prev_max = -1
            for i in range(0, n, k):
                drops = 0
                drop_idx = -1
                for j in range(k):
                    cur = nums[i + j]
                    nxt = nums[i + (j + 1) % k]
                    if cur > nxt:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            return False

                # Determine min and max of the rotated subarray
                if drops == 0:
                    b_min = b_max = nums[i]
                else:
                    b_min = nums[i + (drop_idx + 1) % k]
                    b_max = nums[i + drop_idx]

                if b_min < prev_max:
                    return False
                prev_max = b_max

            return True

        # Sum all valid divisors k
        return sum(k for k in range(1, n + 1) if n % k == 0 and check(k))