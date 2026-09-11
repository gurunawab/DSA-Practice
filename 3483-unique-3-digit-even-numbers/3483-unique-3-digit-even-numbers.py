from collections import Counter


class Solution:

  def totalNumbers(self, digits: list[int]) -> int:
    count = Counter(digits)
    ans = 0

    # Iterate through all possible 3-digit even numbers
    for x in range(100, 1000, 2):
      req = Counter(map(int, str(x)))
      # Check if available digits satisfy required digits
      if all(count[d] >= req[d] for d in req):
        ans += 1

    return ans