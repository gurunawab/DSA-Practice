from collections import deque


class Solution:

  def catMouseGame(self, graph: list[list[int]]) -> int:
    n = len(graph)
    # color[m][c][turn]: 1=Mouse win, 2=Cat win, 0=Draw
    color, degree = {}, {}
    q = deque()

    for m in range(n):
      for c in range(1, n):
        degree[m, c, 1] = len(graph[m])
        degree[m, c, 2] = len([v for v in graph[c] if v != 0])
        if m == 0:
          color[m, c, 1] = color[m, c, 2] = 1
          q.extend([(m, c, 1), (m, c, 2)])
        elif m == c:
          color[m, c, 1] = color[m, c, 2] = 2
          q.extend([(m, c, 1), (m, c, 2)])

    def get_parents(m, c, turn):
      if turn == 1:
        return [
            (m, c_prev, 2) for c_prev in graph[c] if c_prev != 0
        ]  # Cat moved last
      return [(m_prev, c, 1) for m_prev in graph[m]]  # Mouse moved last

    while q:
      m, c, turn = q.popleft()
      win_color = color[m, c, turn]

      for pm, pc, pturn in get_parents(m, c, turn):
        if (pm, pc, pturn) in color:
          continue
        if pturn == win_color:  # Active player can move to a winning state
          color[pm, pc, pturn] = win_color
          q.append((pm, pc, pturn))
        else:
          degree[pm, pc, pturn] -= 1
          if (
              degree[pm, pc, pturn] == 0
          ):  # All moves lead to opponent win -> loss
            color[pm, pc, pturn] = win_color
            q.append((pm, pc, pturn))

    return color.get((1, 2, 1), 0)