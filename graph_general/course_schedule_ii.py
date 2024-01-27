from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for src, dest in prerequisites:
            adj_list[dest].append(src)
            indegree[src] += 1

        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for adj in adj_list[course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        return order if len(order) == numCourses else []
