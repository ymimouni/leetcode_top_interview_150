from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [1] * n

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m and col < n and obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif row == m - 1 and col < n - 1:
                    dp[col] = dp[col + 1]
                elif row < m - 1 and col < n - 1:
                    dp[col] += dp[col + 1]

        return dp[0]


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])

#         @lru_cache(maxsize=None)
#         def dfs(row: int, col: int) -> int:
#             if row < 0 or row >= m or col < 0 or col >= n or obstacleGrid[row][col] == 1:
#                 return 0

#             if row == m - 1 and col == n - 1:
#                 return 1

#             return dfs(row + 1, col) + dfs(row, col + 1)

#         return dfs(0, 0)
