from typing import List


class Solution:
    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #         def r_coin_change(idx, coins, amount):
    #             if amount == 0:
    #                 return 0
    #             elif idx >= len(coins) or amount < 0:
    #                 return -1
    #             else:
    #                 min_cost = float("inf")
    #                 for i in range(idx, len(coins)):
    #                     res = r_coin_change(i, coins, amount - coins[i])
    #                     if res != -1:
    #                         min_cost = min(min_cost, res + 1)
    #                 return min_cost if min_cost != float("inf") else -1

    #         return r_coin_change(0, coins, amount)

    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #         def r_coin_change(coins, rem, count):
    #             if rem == 0:
    #                 return 0
    #             elif rem < 0:
    #                 return -1
    #             elif count[rem - 1]:
    #                 return count[rem - 1]
    #             else:
    #                 min_cost = float("inf")
    #                 for coin in coins:
    #                     res = r_coin_change(coins, rem - coin, count)
    #                     if res != -1:
    #                         min_cost = min(min_cost, res + 1)
    #                 count[rem - 1] = min_cost if min_cost != float("inf") else -1
    #                 return count[rem - 1]

    #         count = [None] * amount
    #         return r_coin_change(coins, amount, count)

    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            dp[x] = min((dp[x - coin] + 1 for coin in coins if coin <= x), default=INF)

        return dp[amount] if dp[amount] != INF else -1
