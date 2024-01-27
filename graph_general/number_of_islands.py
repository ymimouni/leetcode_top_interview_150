from typing import List


class Solution:
    class UnionFind:
        def __init__(self, n: int, x) -> None:
            self.parent = [i for i in range(n)]
            self.rank = [0] * n
            self.num_sets = x

        def find(self, x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x: int, y: int) -> bool:
            x_parent = self.find(x)
            y_parent = self.find(y)

            if x_parent != y_parent:
                if self.rank[x_parent] > self.rank[y_parent]:
                    self.parent[y_parent] = x_parent
                elif self.rank[x_parent] < self.rank[y_parent]:
                    self.parent[x_parent] = y_parent
                else:
                    self.parent[y_parent] = x_parent
                    self.rank[x_parent] += 1
                self.num_sets -= 1
                return True

            return False

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        union_find = self.UnionFind(m * n, sum(1 for i in range(m) for j in range(n) if grid[i][j] == '1'))
        directions = [(0, 1), (1, 0)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    for d in directions:
                        new_row, new_col = row + d[0], col + d[1]
                        if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1'\
                                and grid[new_row][new_col] == '1':
                            union_find.union(row * n + col, new_row * n + new_col)
                    grid[row][col] = '0'

        return union_find.num_sets


# from typing import Tuple


# class Solution:
#     class UnionFind:
#         def __init__(self, n: int) -> None:
#             self.parent = [i for i in range(n)]
#             self.rank = [0] * (n)

#         def find(self, x: int) -> int:
#             if self.parent[x] != x:
#                 self.parent[x] = self.find(self.parent[x])
#             return self.parent[x]

#         def union(self, x: int, y: int) -> bool:
#             x_parent = self.find(x)
#             y_parent = self.find(y)

#             if x_parent != y_parent:
#                 if self.rank[x_parent] > self.rank[y_parent]:
#                     self.parent[y_parent] = x_parent
#                 elif self.rank[x_parent] < self.rank[y_parent]:
#                     self.parent[x_parent] = y_parent
#                 else:
#                     self.parent[y_parent] = x_parent
#                     self.rank[x_parent] += 1
#                 return True

#             return False

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     union_find = self.UnionFind(m*n)
    #     directions = [(0,1), (1,0)]
    #     ans = 0
    #
    #     for row in range(m):
    #         for col in range(n):
    #             if grid[row][col] == '1':
    #                 ans += 1
    #                 for d in directions:
    #                     new_row, new_col = row + d[0], col + d[1]
    #                     if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1'\
    #                             and grid[new_row][new_col] == '1':
    #                         if union_find.union(row * n + col, new_row * n + new_col):
    #                             ans -= 1
    #                 grid[row][col] = '0'
    #
    #     return ans


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(cur_row, cur_col):
#             directions = [(0,1), (1,0), (0,-1), (-1,0)]
#
#             for d in directions:
#                 new_row, new_col = cur_row + d[0], cur_col + d[1]
#                 if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1'\
#                         and (new_row, new_col) not in visited:
#                     visited.add((new_row, new_col))
#                     dfs(new_row, new_col)
#
#         visited = set()
#
#         num_islands = 0
#         m, n = len(grid), len(grid[0])
#         for row in range(m):
#             for col in range(n):
#                 print(grid[row][col])
#                 if grid[row][col] == '1' and (row, col) not in visited:
#                     visited.add((row, col))
#                     dfs(row, col)
#                     num_islands += 1
#
#         return num_islands


# from collections import deque


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def bfs(row, col):
#             directions = [(0,1), (1,0), (0,-1), (-1,0)]
#             queue = deque([(row, col)])
#
#             while queue:
#                 cur_row, cur_col = queue.popleft()
#                 for d in directions:
#                     new_row, new_col = cur_row + d[0], cur_col + d[1]
#                     if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == '1'\
#                             and (new_row, new_col) not in visited:
#                         queue.append((new_row, new_col))
#                         visited.add((new_row, new_col))
#
#         visited = set()
#
#         num_islands = 0
#         m, n = len(grid), len(grid[0])
#         for row in range(m):
#             for col in range(n):
#                 print(grid[row][col])
#                 if grid[row][col] == '1' and (row, col) not in visited:
#                     visited.add((row, col))
#                     bfs(row, col)
#                     num_islands += 1
#
#         return num_islands
