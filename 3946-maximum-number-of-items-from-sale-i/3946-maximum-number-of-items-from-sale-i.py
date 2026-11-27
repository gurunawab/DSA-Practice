class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free_count = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free_count[i] += 1

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor, price = items[i]
            val1 = 1 + free_count[i]

            temp = [-1] * (budget + 1)

            # First copy
            for w in range(price, budget + 1):
                if dp[w - price] != -1:
                    temp[w] = dp[w - price] + val1

            # Subsequent copies
            for w in range(price, budget + 1):
                if temp[w - price] != -1:
                    temp[w] = max(temp[w], temp[w - price] + 1)

            # Merge
            for w in range(budget + 1):
                if temp[w] > dp[w]:
                    dp[w] = temp[w]

        return max(dp)