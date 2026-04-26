#Common in 3 Sorted Arrays
def commonElements(self, a, b, c):
        common = set(a) & set(b) & set(c)
        
        return sorted(list(common))