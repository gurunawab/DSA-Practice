class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        
        k -= 1
        res = ["abc"[k // (1 << (n - 1))]]
        
        for i in range(n - 2, -1, -1):
            choices = [c for c in "abc" if c != res[-1]]
            res.append(choices[(k >> i) & 1])
            
        return "".join(res)