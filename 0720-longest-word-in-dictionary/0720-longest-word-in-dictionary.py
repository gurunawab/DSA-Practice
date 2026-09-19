class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        valid = {""}
        ans = ""
        
        for w in words:
            if w[:-1] in valid:
                valid.add(w)
                if len(w) > len(ans):
                    ans = w
                    
        return ans