class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, event_type, time_str = log.split(":")
            fn_id = int(fn_id_str)
            timestamp = int(time_str)

            if event_type == "start":
                if stack:
                    
                    result[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:  
                
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return result