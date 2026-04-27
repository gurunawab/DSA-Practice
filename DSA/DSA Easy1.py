#Common in 3 Sorted Arrays
def commonElements(self, a, b, c):
        common = set(a) & set(b) & set(c)
        
        return sorted(list(common))

#Smallest window containing 0, 1 and 2
def smallestSubstring(self, s):
        pos = {'0':-1, '1':-1, '2':-1}
        min_len = float('inf')
        
        for i, char in enumerate(s):
            pos[char] = i
            
            if -1 not in pos.values():
                min_len = min(min_len, i - min(pos.values()) + 1)
                
        return min_len if min_len != float('inf') else -1                