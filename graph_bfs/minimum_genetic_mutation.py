from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(0, startGene)])
        seen = {startGene}

        while queue:
            d, curr = queue.popleft()

            if curr == endGene:
                return d

            for c in "ACGT":
                for i in range(8):
                    neighbor = curr[:i] + c + curr[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((d + 1, neighbor))
                        seen.add(neighbor)

        return -1


# class Solution:
#     def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
#         bank = set(bank)
#         min_dist = float("inf")
#         visited = set()

#         def helper(start: str, end: str, distance: int) -> None:
#             nonlocal min_dist

#             visited.add(start)

#             if start == end:
#                 min_dist = min(min_dist, distance)
#                 return None

#             for i in range(8):
#                 for c in {'A', 'C', 'G', 'T'}:
#                     new_start = start[:i] + c + start[i + 1:]
#                     if new_start not in visited and new_start in bank:
#                         helper(new_start, end, distance + 1)

#         helper(startGene, endGene, 0)

#         return min_dist if min_dist != float("inf") else -1
