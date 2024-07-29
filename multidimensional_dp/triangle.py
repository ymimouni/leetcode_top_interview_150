from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        below_row = triangle[-1]
        for row in range(n - 2, -1, -1):
            cur_row = []
            for col in range(len(triangle[row])):
                cur_row.append(triangle[row][col] + min(below_row[col], below_row[col + 1]))
            below_row = cur_row

        return below_row[0]


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         for row in range(n - 2, -1, -1):
#             for col in range(len(triangle[row])):
#                 triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

#         return triangle[0][0]


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         @lru_cache(maxsize=None)
#         def dfs(row: int, col: int) -> int:
#             path = triangle[row][col]
#             if row < n - 1:
#                 path += min(dfs(row + 1, col), dfs(row + 1, col + 1))
#             return path

#         return dfs(0, 0)
