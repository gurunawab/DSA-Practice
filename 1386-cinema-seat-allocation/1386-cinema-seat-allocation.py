from collections import defaultdict


class Solution:

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    rows = defaultdict(int)
    for r, c in reservedSeats:
      if 1 < c < 10:
        rows[r] |= 1 << (c - 2)

    ans = (n - len(rows)) * 2
    for mask in rows.values():
      left = not (mask & 0b00001111)  # seats 2, 3, 4, 5
      right = not (mask & 0b11110000)  # seats 6, 7, 8, 9
      mid = not (mask & 0b00111100)  # seats 4, 5, 6, 7

      if left and right:
        ans += 2
      elif left or right or mid:
        ans += 1

    return ans