from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        cost = [float("inf")] * (k + 1)
        profit = [0] * (k + 1)

        for price in prices:
            for i in range(k):
                cost[i + 1] = min(cost[i + 1], price - profit[i])
                profit[i + 1] = max(profit[i + 1], price - cost[i + 1])

        return profit[-1]
