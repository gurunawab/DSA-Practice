class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
        count = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
           
            if count[sandwich] == 0:
                break
            
            count[sandwich] -= 1
            
        
        return sum(count)