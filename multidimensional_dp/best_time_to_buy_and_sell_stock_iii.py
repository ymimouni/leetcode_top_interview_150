from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit


# class Solution(object):
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)

#         left_profits = [0] * n
#         left_min = prices[0]

#         for i, price in enumerate(prices):
#             left_min = min(left_min, price)
#             left_profits[i] = max(left_profits[i - 1], price - left_min)

#         right_profit = 0
#         right_max = prices[-1]
#         profit = left_profits[-1]

#         for i in range(n - 1, 1, -1):
#             right_max = max(right_max, prices[i])
#             right_profit = max(right_profit, right_max - prices[i])
#             profit = max(profit, right_profit + left_profits[i - 1])

#         return profit
