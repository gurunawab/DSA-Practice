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

#Non-Attacking Black and White Knights
def numOfWays(self, n: int, m: int) -> int:
       
        total_squares = n * m
        
        
        total_ways = total_squares * (total_squares - 1)
        
       
        attacking_2x3 = 0
        if n >= 2 and m >= 3:
            attacking_2x3 = (n - 1) * (m - 2)
            
        
        attacking_3x2 = 0
        if n >= 3 and m >= 2:
            attacking_3x2 = (n - 2) * (m - 1)
            
       
        total_attacking_ways = 4 * (attacking_2x3 + attacking_3x2)
        
        
        return total_ways - total_attacking_ways


 
#Create Binary Tree From Descriptions
def createBinaryTree(self, descriptions):
        
        nodes = {}
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]
            
            
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]
            
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            
            children.add(child_val)
            
        
        for parent_val in nodes:
            if parent_val not in children:
                return nodes[parent_val]        