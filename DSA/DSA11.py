#Lexicographically smallest after removing k
def lexicographicallySmallest(self, s: str, k: int) -> str:
        n = len(s)
        
        
        is_power_of_2 = (n > 0) and (n & (n - 1)) == 0
        
        
        if is_power_of_2:
            k = k // 2
        else:
            k = k * 2
            
        
        if k >= n or n == 0:
            return "-1"
            
        
        stack = []
        removals_left = k
        
        for char in s:
            
            while stack and removals_left > 0 and stack[-1] > char:
                stack.pop()
                removals_left -= 1
            stack.append(char)
            
        
        if removals_left > 0:
            stack = stack[:-removals_left]
            
        return "".join(stack)