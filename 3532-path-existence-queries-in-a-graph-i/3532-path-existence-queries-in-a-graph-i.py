class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # component_id[i] will store the ID of the connected component node i belongs to
        component_id = [0] * n
        curr_id = 0
        
       
        for i in range(1, n):
            # If the difference between adjacent elements > maxDiff, 
            # a new component starts
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # Process each query in O(1)
        results = []
        for u, v in queries:
            results.append(component_id[u] == component_id[v])
            
        return results