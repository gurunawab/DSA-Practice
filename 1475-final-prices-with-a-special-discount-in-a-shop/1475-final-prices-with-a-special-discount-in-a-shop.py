class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = list(prices)
        stack = []  

        for i in range(len(prices)):
            
            while stack and prices[stack[-1]] >= prices[i]:
                prev_idx = stack.pop()
                ans[prev_idx] -= prices[i]
            stack.append(i)

        return ans