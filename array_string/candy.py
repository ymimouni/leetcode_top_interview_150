from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)

    # def candy(self, ratings: List[int]) -> int:
    #     i = j = 0
    #     n = len(ratings)
    #     min_candies = [1] * n

    #     while i < n - 1:
    #         j = i
    #         while j < n - 1 and ratings[j] > ratings[j + 1]:
    #             j += 1

    #         for k in range(j - 1, i - 1, -1):
    #             min_candies[k] = max(min_candies[k], min_candies[k + 1] + 1)

    #         while j < n - 1 and ratings[j] == ratings[j + 1]:
    #             j += 1

    #         while j < n - 1 and ratings[j] < ratings[j + 1]:
    #             min_candies[j + 1] = min_candies[j] + 1
    #             j += 1

    #         while j < n - 1 and ratings[j] == ratings[j + 1]:
    #             j += 1

    #         i = j

    #     return sum(min_candies)
