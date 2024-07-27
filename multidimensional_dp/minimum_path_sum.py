from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [0] * n
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    dp[col] = grid[row][col]
                elif col == n - 1:
                    dp[col] += grid[row][col]
                elif row == m - 1:
                    dp[col] = grid[row][col] + dp[col + 1]
                else:
                    dp[col] = grid[row][col] + min(dp[col], dp[col + 1])

        return dp[0]


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])

#         @lru_cache(maxsize=None)
#         def dfs(row: int, col: int) -> int:
#             path = grid[row][col]
#             if row < m - 1 and col < n - 1:
#                 path += min(dfs(row + 1, col), dfs(row, col + 1))
#             elif row < m - 1:
#                 path += dfs(row + 1, col)
#             elif col < n - 1:
#                 path += dfs(row, col + 1)

#             return path

#         return dfs(0, 0)
