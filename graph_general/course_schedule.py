from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for (a, b) in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        visited = 0
        while queue:
            course = queue.popleft()
            visited += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     def dfs(course):
    #         if in_stack[course]:
    #             return True
    #         if visited[course]:
    #             return False
    #         visited[course] = True
    #         in_stack[course] = True
    #         for prerequisite in adj[course]:
    #             if dfs(prerequisite):
    #                 return True
    #         in_stack[course] = False
    #         return False

    #     # Step 1 - Create the adjacency list.
    #     adj = [[] for _ in range(numCourses)]
    #     for (a, b) in prerequisites:
    #         adj[a].append(b)

    #     # Step 2 - DFS with backtracking.
    #     visited = [False] * numCourses
    #     in_stack = [False] * numCourses
    #     for course in range(numCourses):
    #         if dfs(course):
    #             return False

    #     return True
