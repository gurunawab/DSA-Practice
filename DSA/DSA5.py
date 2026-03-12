#Subarrays with First Element Minimum
def countSubarrays(self, arr):
        n = len(arr)
        
        nse = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                nse[index] = i
            stack.append(i)
            
        ans = 0
        
        for i in range(n):
            ans += (nse[i] - i)
            
        return ans 


#Sum of subarray minimums
def sumSubMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        stack = []    
            
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        total_sum = 0
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            total_sum += count * arr[i]
            
        return total_sum 


#Minimum K Consecutive Bit Flips
def kBitFlips(self, arr, k):
        n = len(arr)
        
        diff = [0] * (n + 1)
        total_flips = 0
        current_flips = 0
        
        for i in range(n):
            current_flips += diff[i]
            
            if (arr[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                    
                total_flips += 1
                current_flips += 1
                diff[i + k] -= 1
                
        return total_flips 


#Maximize Spanning Tree Stability with Upgrades
def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        def can_achieve(mid):
            parent = list(range(n))
            def find(i):
                if parent[i] == i: return i
                parent[i] = find(parent[i])
                return parent[i]

            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    return True
                return False

            edges_count = 0
            upgrades_used = 0

            for u, v, s, must in edges:
                if must == 1:
                    if s < mid: return False
                    if not union(u, v): return False
                    edges_count += 1

            for u, v, s, must in edges:
                if must == 0 and s >= mid:
                    if union(u, v):
                        edges_count += 1

            for u, v, s, must in edges:
                if must == 0 and s < mid and s * 2 >= mid:
                    if upgrades_used < k:
                        if union(u, v):
                            edges_count += 1
                            upgrades_used += 1

            return edges_count == n - 1

        low, high = 0, 2 * 10**5
        ans = -1

        if not can_achieve(0): return -1

        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
                   
        