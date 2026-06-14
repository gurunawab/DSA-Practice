#Maximum Twin Sum of a Linked List
def pairSum(self, head):
        
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
       
        
        
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        
        
        
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            current_twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_twin_sum)
            
           
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum

#Exit Point in a Matrix
def exitPoint(self, mat: list[list[int]]) -> list[int]:
        
        n = len(mat)
        m = len(mat[0])
        
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
       
        i, j = 0, 0
        dir_idx = 0
        
        
        last_i, last_j = 0, 0
        
        while 0 <= i < n and 0 <= j < m:
           
            last_i, last_j = i, j
            
            
            if mat[i][j] == 1:
                mat[i][j] = 0
                dir_idx = (dir_idx + 1) % 4
            
           
            i += directions[dir_idx][0]
            j += directions[dir_idx][1]
            
        return [last_i, last_j]