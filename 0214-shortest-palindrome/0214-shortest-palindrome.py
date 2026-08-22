class Solution:
    def shortestPalindrome(self, s: str) -> str:
        temp = s + "#" + s[::-1]
        pi = [0] * len(temp)
        
        for i in range(1, len(temp)):
            j = pi[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = pi[j - 1]
            if temp[i] == temp[j]:
                j += 1
            pi[i] = j
            
        return s[pi[-1]:][::-1] + s