from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        prev = float("inf")
        for price in prices:
            if prev < price:
                max_profit += price - prev
            prev = price

        return max_profit
