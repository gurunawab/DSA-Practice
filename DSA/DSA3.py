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
        """
        :type s: str
        :rtype: int
        """
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
        