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