from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
    
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + int(s[i])
            
       
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
      
        non_zero_indices = [i for i, char in enumerate(s) if char != '0']
      
        non_zero_vals = [int(s[i]) for i in non_zero_indices]
        
       
        nz_count = len(non_zero_indices)
        pref_hashes = [0] * (nz_count + 1)
        for i in range(nz_count):
            pref_hashes[i+1] = (pref_hashes[i] * 10 + non_zero_vals[i]) % MOD
            
        import bisect
        
        results = []
        for l, r in queries:
         
            digit_sum = pref_sum[r+1] - pref_sum[l]
            
           
            idx_start = bisect.bisect_left(non_zero_indices, l)
            idx_end = bisect.bisect_right(non_zero_indices, r)
            
            count = idx_end - idx_start
            
            if count == 0:
                results.append(0)
            else:
               
                x = (pref_hashes[idx_end] - (pref_hashes[idx_start] * pow10[count])) % MOD
                results.append((x * digit_sum) % MOD)
                
        return results