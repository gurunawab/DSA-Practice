#Print Diagonally
def diagView(self, mat): 
        n =len(mat)
        result = []
        
        for s in range(2 * n - 1):
            start_i = max(0, s - (n - 1))
            
            end_i = min(s, n -1)
            
            for i in range(start_i, end_i + 1):
                j = s - i
                result.append(mat[i][j])
                
        return result 


#Painting the Fence
def countWays(self,n,k):
        if n == 1:
            return k
            
        same = k
        diff = k * (k - 1)
        total = same + diff
        
        for i in range(3, n + 1):
            same = diff
            diff = total * (k - 1)
            total = same + diff
            
        return total  

  