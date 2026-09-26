class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    rows, cols, boxes = (
        [set() for _ in range(9)],
        [set() for _ in range(9)],
        [set() for _ in range(9)],
    )
    empty = []

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          empty.append((r, c))
        else:
          rows[r].add(val)
          cols[c].add(val)
          boxes[(r // 3) * 3 + c // 3].add(val)

    def solve(idx=0):
      if idx == len(empty):
        return True
      r, c = empty[idx]
      b = (r // 3) * 3 + c // 3

      for val in map(str, range(1, 10)):
        if (
            val not in rows[r]
            and val not in cols[c]
            and val not in boxes[b]
        ):
          rows[r].add(val)
          cols[c].add(val)
          boxes[b].add(val)
          board[r][c] = val

          if solve(idx + 1):
            return True

          rows[r].remove(val)
          cols[c].remove(val)
          boxes[b].remove(val)
          board[r][c] = "."
      return False

    solve()