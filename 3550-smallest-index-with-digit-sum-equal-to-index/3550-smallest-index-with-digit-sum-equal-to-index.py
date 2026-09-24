class Solution:

  def smallestIndex(self, nums: list[int]) -> int:
    return next(
        (
            i
            for i, x in enumerate(nums)
            if sum(int(digit) for digit in str(x)) == i
        ),
        -1,
    )