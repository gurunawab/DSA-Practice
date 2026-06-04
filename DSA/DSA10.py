#Count Sorted Digit Groupings
from functools import lru_cache

class Solution:
    def validGroups(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def solve(index, prev_sum):
            
            if index == n:
                return 1
            
            current_sum = 0
            ways = 0
            
           
            for j in range(index, n):
                current_sum += int(s[j])
                
                
                if current_sum >= prev_sum:
                    ways += solve(j + 1, current_sum)
                    
            return ways

       
        return solve(0, 0)
    
#Total Waviness of Numbers in Range I
def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
        def solve(N):
            if N < 0:
                return 0
            s = str(N)
            L = len(s)
            
            
            memo = {}
            
            def dp(idx, prev_digit, trend, is_less, is_started):
                
                if idx == L:
                    return 0
                
                state = (idx, prev_digit, trend, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                ans = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            
                            ans += dp(idx + 1, -1, 0, next_less, False)
                        else:
                            
                            ans += dp(idx + 1, d, 0, next_less, True)
                    else:
                        
                        wavy_contribution = 0
                        next_trend = 0
                        
                        if prev_digit != -1:
                            if d > prev_digit:
                                next_trend = 1  
                                
                                if trend == 2:
                                    wavy_contribution = 1
                            elif d < prev_digit:
                                next_trend = 2  
                                
                                if trend == 1:
                                    wavy_contribution = 1
                            else:
                                next_trend = 0  
                        
                         
                        if wavy_contribution > 0:
                            ans += count_ways(idx + 1, d, next_less, True)
                            
                        
                        ans += dp(idx + 1, d, next_trend, next_less, True)
                        
                memo[state] = ans
                return ans

            
            count_memo = {}
            def count_ways(idx, prev_digit, is_less, is_started):
                if idx == L:
                    return 1 if is_started else 0
                state = (idx, prev_digit, is_less, is_started)
                if state in count_memo:
                    return count_memo[state]
                
                limit = 9 if is_less else int(s[idx])
                ans = 0
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    if not is_started and d == 0:
                        ans += count_ways(idx + 1, -1, next_less, False)
                    else:
                        ans += count_ways(idx + 1, d, next_less, True)
                count_memo[state] = ans
                return ans

            return dp(0, -1, 0, False, False)

        return solve(num2) - solve(num1 - 1)    

#Earliest Finish Time for Land and Water Rides II
import bisect

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)
        
       
        land = sorted(zip(landStartTime, landDuration), key=lambda x: x[0])
        l_starts = [x[0] for x in land]
        l_durs = [x[1] for x in land]
        l_fins = [x[0] + x[1] for x in land]
        
       
        water = sorted(zip(waterStartTime, waterDuration), key=lambda x: x[0])
        w_starts = [x[0] for x in water]
        w_durs = [x[1] for x in water]
        w_fins = [x[0] + x[1] for x in water]
        
        
        def get_suffix_mins(starts, durs, fins):
            k = len(starts)
            suffix_dur = [float('inf')] * (k + 1)
            suffix_fin = [float('inf')] * (k + 1)
            for i in range(k - 1, -1, -1):
                suffix_dur[i] = min(suffix_dur[i+1], durs[i])
                suffix_fin[i] = min(suffix_fin[i+1], fins[i])
            return suffix_dur, suffix_fin
            
        l_suffix_dur, l_suffix_fin = get_suffix_mins(l_starts, l_durs, l_fins)
        w_suffix_dur, w_suffix_fin = get_suffix_mins(w_starts, w_durs, w_fins)
        
        
        def get_prefix_mins(durs):
            prefix_dur = []
            curr_min = float('inf')
            for d in durs:
                curr_min = min(curr_min, d)
                prefix_dur.append(curr_min)
            return prefix_dur

        l_prefix_dur = get_prefix_mins(l_durs)
        w_prefix_dur = get_prefix_mins(w_durs)
        
        ans = float('inf')
        
     
        for i in range(n):
            f_land = l_fins[i]
         
            idx = bisect.bisect_right(w_starts, f_land)
            
           
            if idx > 0:
                ans = min(ans, f_land + w_prefix_dur[idx - 1])
         
            if idx < m:
                ans = min(ans, w_suffix_fin[idx])
                
    
        for j in range(m):
            f_water = w_fins[j]
          
            idx = bisect.bisect_right(l_starts, f_water)
            
            
            if idx > 0:
                ans = min(ans, f_water + l_prefix_dur[idx - 1])
          
            if idx < n:
                ans = min(ans, l_suffix_fin[idx])
                
        return ans
    
#Subarray Frequency Count Queries
from collections import defaultdict
import bisect

class Solution:
    def freqInRange(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        
        pos_map = defaultdict(list)
        for index, num in enumerate(arr):
            pos_map[num].append(index)
            
        result = []
        
    
        for l, r, x in queries:
            if x not in pos_map:
                result.append(0)
                continue
                
            indices = pos_map[x]
            
            
            left_bound = bisect.bisect_left(indices, l)
           
            right_bound = bisect.bisect_right(indices, r)
            
            
            count = right_bound - left_bound
            result.append(count)
            
        return result     