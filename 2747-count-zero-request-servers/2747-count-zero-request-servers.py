from collections import defaultdict
from typing import List


class Solution:

  def countServers(
      self, n: int, logs: List[List[int]], x: int, queries: List[int]
  ) -> List[int]:
    logs.sort(key=lambda log: log[1])
    sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])

    ans = [0] * len(queries)
    server_count = defaultdict(int)
    left = right = 0
    m = len(logs)

    for original_idx, q_time in sorted_queries:
      start_time = q_time - x

      # Expand right boundary: include logs up to q_time
      while right < m and logs[right][1] <= q_time:
        server_count[logs[right][0]] += 1
        right += 1

      # Shrink left boundary: exclude logs before start_time
      while left < m and logs[left][1] < start_time:
        server_id = logs[left][0]
        server_count[server_id] -= 1
        if server_count[server_id] == 0:
          del server_count[server_id]
        left += 1

      ans[original_idx] = n - len(server_count)

    return ans