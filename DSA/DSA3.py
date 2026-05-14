#Longest Substring with K uniques
def longestkSubstr(self, s, k):
    char_map = {}
    i = 0
    max_len = -1

    for j in range(len(s)):
        char_map[s[j]] = char_map.get(s[j], 0) + 1

        while len(char_map) > k:
            char_map[s[j]] -= 1
            if char_map[s[i]] == 0:
                del char_map[s[i]]
            i += 1

        if len(char_map) == k:
            max_len = max(max_len, j - i + 1)

    return max_len      

 

#Smallest Window containing all characters
from collections import Counter

class Solution:
    def minWindow(self, s, p):
        if not s or not p:
            return ""
        
       
        p_count = Counter(p)
        required = len(p_count)
        
        
        window_count = {}
        formed = 0
        
        
        ans = float("inf"), None, None
        
        start = 0
        for end in range(len(s)):
            char = s[end]
            window_count[char] = window_count.get(char, 0) + 1
            

            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
            
            
            while start <= end and formed == required:
                char = s[start]
                
                
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                
                
                window_count[char] -= 1
                if char in p_count and window_count[char] < p_count[char]:
                    formed -= 1
                
                start += 1
                
        return "" if ans[1] is None else s[ans[1] : ans[2] + 1]      


#Dice Throw
class Solution:
    def noOfWays(self, m,n,x):
        
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, x + 1):
                for k in range(1, m + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i-1][j-k]
                        
        return dp[n][x]  


#Minimum Number of flips to Make the Binary String Alternating
def minFlips(self, s):
      
        n = len(s)
        s = s + s

        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"

        res = len(s)
        diff1, diff2 = 0, 0
        l = 0

        for r in range(len(s)):

            if s[r] != target1[r]:
                diff1 += 1

            if s[r] != target2[r]:
                diff2 += 1

            if (r - l + 1) > n:

                if s[l] != target1[l]:
                    diff1 -= 1

                if s[l] != target2[l]:
                    diff2 -= 1

                l += 1

            if (r - l + 1) == n:
                res = min(res, diff1, diff2)

        return res         


#Minimum cost to connect all houses in a city
import heapq


def minCost(self, houses):
        n = len(houses)
        if n == 0:
            return 0
        
        # min_heap stores (cost, current_house_index)
        min_heap = [(0, 0)]
        visited = [False] * n
        total_cost = 0
        edges_count = 0
        
        while edges_count < n:
            cost, u = heapq.heappop(min_heap)
            
           
            if visited[u]:
                continue
            
          
            visited[u] = True
            total_cost += cost
            edges_count += 1
            
         
            for v in range(n):
                if not visited[v]:
                    # Manhattan Distance calculation
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    heapq.heappush(min_heap, (dist, v))
                    
        return total_cost         


#Maximum Walls Destroyed by Robots
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            left = arr[i][0] - arr[i][1]
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)
            l = bisect_left(walls, left)
            r = bisect_left(walls, arr[i][0] + 1)
            ans = dfs(i - 1, 0) + r - l
            right = arr[i][0] + arr[i][1]
            if i + 1 < n:
                if j == 0:
                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                else:
                    right = min(right, arr[i + 1][0] - 1)
            l = bisect_left(walls, arr[i][0])
            r = bisect_left(walls, right + 1)
            ans = max(ans, dfs(i - 1, 1) + r - l)
            return ans

        return dfs(n - 1, 1)


#Decode the Slanted Ciphertext
def decodeCiphertext(self, encodedText, rows):
        
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        res = []

        for start_col in range(cols):
            curr_row = 0
            curr_col = start_col

            while curr_row < rows and curr_col < cols:
                index = curr_row * cols + curr_col
                res.append(encodedText[index])

                curr_row += 1
                curr_col += 1 

        return "".join(res).rstrip()   

#Maximize the Distance Between Points on a Square
def maxDistance(self, side, points, k):
       
        arr = []
        for x, y in points:
            if y == 0: arr.append(x)
            elif x == side: arr.append(side + y)
            elif y == side: arr.append(2 * side + (side - x))
            else: arr.append(3 * side + (side - y))
        
        arr.sort()
        n = len(arr)
        perimeter = 4 * side
        
        
        def check(mid):
           
            for i in range(n):
               
                if arr[i] - arr[0] > mid:
                    break
                
                count = 1
                last = arr[i]
                target = last + mid
                
               
                import bisect
                curr_idx = i
                for _ in range(k - 1):
                    
                    curr_idx = bisect.bisect_left(arr, target, lo=curr_idx + 1)
                    if curr_idx == n:
                        break
                    last = arr[curr_idx]
                    target = last + mid
                else:
                    
                    if perimeter - (last - arr[i]) >= mid:
                        return True
            return False

        
        low, high = 1, 2 * side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans  

#Minimum Moves to Make Array Complementary
def minMoves(self, nums, limit):
        
        diff = [0] * (2 * limit + 2)
        n = len(nums)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b:
                a, b = b, a

            diff[2] += 2
            diff[2 * limit + 1] -= 2

            diff[a + 1] -= 1
            diff[limit + b + 1] += 1

            diff[a + b] -= 1
            diff[a + b + 1] += 1

        current_moves = 0
        min_moves = n

        for s in range(2, 2 * limit + 1):
            current_moves += diff[s]
            min_moves = min(min_moves, current_moves)

        return min_moves

#Mother Vertex
def findMotherVertex(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        visited = [False] * V
        last_v = 0
        
        def dfs(node, vis):
            vis[node] = True
            for nbr in adj[node]:
                if not vis[nbr]:
                    dfs(nbr, vis)
                    
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                last_v = i
                
        visited = [False] * V
        dfs(last_v, visited)
        
        return last_v if all(visited) else -1      
                                            
        