class Solution(object):

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]

        :rtype: List[int]
        """
       
        temp = sorted(nums)

        
        d = {}
        for index, num in enumerate(temp):
            if num not in d:
                d[num] = index

        
        return [d[num] for num in nums]