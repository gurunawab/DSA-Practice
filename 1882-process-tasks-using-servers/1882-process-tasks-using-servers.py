import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = []
        time = 0
        
        for j, task_duration in enumerate(tasks):
            time = max(time, j)
            
            if not free_servers and busy_servers[0][0] > time:
                time = busy_servers[0][0]
                
            while busy_servers and busy_servers[0][0] <= time:
                _, weight, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, server_idx))
                
            weight, server_idx = heapq.heappop(free_servers)
            ans.append(server_idx)
            heapq.heappush(busy_servers, (time + task_duration, weight, server_idx))
            
        return ans