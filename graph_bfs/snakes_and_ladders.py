import heapq
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [-1] * (n ** 2 + 1)
        cols = list(range(n))
        label = 1
        for row in range(n - 1, -1, -1):
            for col in cols:
                cells[label] = (row, col)
                label += 1
            cols.reverse()

        dist = [-1] * (n ** 2 + 1)
        dist[1] = 0
        queue = []
        heapq.heappush(queue, (0, 1))

        while queue:
            distance, curr = heapq.heappop(queue)
            if distance > dist[curr]:
                continue
            for next_ in range(curr + 1, min(curr + 6, n ** 2) + 1):
                row, col = cells[next_]
                next_ = next_ if board[row][col] == -1 else board[row][col]
                if dist[next_] == -1 or 1 + distance < dist[next_]:
                    dist[next_] = distance + 1
                    heapq.heappush(queue, (dist[next_], next_))

        return dist[n ** 2]


# from collections import deque


# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         n = len(board)
#         cells = [-1] * (n ** 2 + 1)
#         cols = list(range(n))
#         label = 1
#         for row in range(n - 1, -1, -1):
#             for col in cols:
#                 cells[label] = (row, col)
#                 label += 1
#             cols.reverse()

#         dist = [-1] * (n ** 2 + 1)
#         dist[1] = 0
#         queue = deque([1])

#         while queue:
#             curr = queue.popleft()
#             for next in range(curr + 1, min(curr + 6, n ** 2 + 1)):
#                 row, col = cells[next]
#                 next = next if board[row][col] == -1 else board[row][col]
#                 if dist[next] == -1:
#                     dist[next] = dist[curr] + 1
#                     queue.append(next)

#         return dist[n ** 2]
