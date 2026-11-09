import heapq
from typing import List


class Solution:

    def busiestServers(
        self, k: int, arrival: List[int], load: List[int]
    ) -> List[int]:
        # Count of requests handled by each server
        count = [0] * k

        # Min-heap of available servers: initially [0, 1, ..., k-1]
        available = list(range(k))
        heapq.heapify(available)

        # Min-heap of busy servers: (end_time, server_id)
        busy = []

        for i, (t, l) in enumerate(zip(arrival, load)):
            # Free up servers jo current arrival time 't' tak free ho chuke hain
            while busy and busy[0][0] <= t:
                _, server_id = heapq.heappop(busy)
                # Virtual ID push karte hain jo >= i ho aur server_id % k match kare
                heapq.heappush(available, i + (server_id - i) % k)

            # Agar koi server available hai
            if available:
                virtual_id = heapq.heappop(available)
                real_server_id = virtual_id % k

                count[real_server_id] += 1
                heapq.heappush(busy, (t + l, real_server_id))

        max_req = max(count)
        return [idx for idx, c in enumerate(count) if c == max_req]