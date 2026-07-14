from fractions import gcd

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        
        dp = {(0, 0): 1}
        
        for x in nums:
            next_dp = {}
            for (g1, g2), count in dp.iteritems(): # Using iteritems() for Python 2 efficiency
                # Choice 1: Don't include x in either sequence
                next_dp[(g1, g2)] = (next_dp.get((g1, g2), 0) + count) % MOD
                
                # Choice 2: Include x in seq1
                ng1 = gcd(g1, x) if g1 != 0 else x
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                # Choice 3: Include x in seq2
                ng2 = gcd(g2, x) if g2 != 0 else x
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), count in dp.iteritems():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans
        