class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  

        for current_day, current_temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < current_temp:
                prev_day = stack.pop()
                answer[prev_day] = current_day - prev_day
            
            
            stack.append(current_day)

        return answer