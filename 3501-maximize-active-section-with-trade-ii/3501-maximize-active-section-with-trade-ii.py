import bisect

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        if self.n == 0:
            return
        self.K = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.K)]
        
        for i in range(self.n):
            self.st[0][i] = arr[i]
            
        for i in range(1, self.K):
            j = 0
            while j + (1 << i) <= self.n:
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    def query(self, L, R):
        if L > R:
            return 0
        length = R - L + 1
        k = length.bit_length() - 1
        return max(self.st[k][L], self.st[k][R - (1 << k) + 1])


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :type rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Identify all contiguous '0' groups with their start and end indices
        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                end = i - 1
                zero_groups.append({'start': start, 'end': end, 'len': end - start + 1})
            else:
                i += 1
                
        num_groups = len(zero_groups)
        
        # Build binary search helper arrays
        ends = [g['end'] for g in zero_groups]
        starts = [g['start'] for g in zero_groups]
        
        # Build Sparse Table for adjacent group sum lengths
        adj_sums = []
        for g in range(num_groups - 1):
            adj_sums.append(zero_groups[g]['len'] + zero_groups[g + 1]['len'])
            
        st = SparseTable(adj_sums)
        
        ans = []
        
        for l, r in queries:
            # Find the first zero group that ends at or after 'l'
            i_first = bisect.bisect_left(ends, l)
            
            # Find the last zero group that starts at or before 'r'
            i_last = bisect.bisect_right(starts, r) - 1
            
            # A trade requires at least two zero groups overlapping with [l, r]
            if i_first >= i_last:
                ans.append(total_ones)
                continue
            
            max_gain = 0
            
            # Helper to calculate net gain from merging zero group i and i+1 inside [l, r]
            def get_gain(i):
                g1 = zero_groups[i]
                g2 = zero_groups[i + 1]
                
                # Truncate group 1 to query boundaries
                len1 = g1['end'] - max(g1['start'], l) + 1
                # Truncate group 2 to query boundaries
                len2 = min(g2['end'], r) - g2['start'] + 1
                
                return len1 + len2

            # Check boundary pair at the start
            max_gain = max(max_gain, get_gain(i_first))
            
            # Check boundary pair at the end
            max_gain = max(max_gain, get_gain(i_last - 1))
            
            # Check internal pairs (where both groups are completely inside [l, r])
            if i_first + 1 <= i_last - 2:
                max_gain = max(max_gain, st.query(i_first + 1, i_last - 2))
                
            ans.append(total_ones + max_gain)
            
        return ans
        