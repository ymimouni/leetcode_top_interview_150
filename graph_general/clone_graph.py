from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(node: Optional['Node']) -> None:
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(val = neighbor.val)
                    dfs(neighbor)
                visited[node].neighbors.append(visited[neighbor])

        visited = {node: Node(val=node.val)}
        dfs(node)
        return visited[node]

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     visited = {node: Node(val = node.val)}

    #     queue = deque([node])
    #     while queue:
    #         n = queue.popleft()
    #         for neighbor in n.neighbors:
    #             if neighbor not in visited:
    #                 visited[neighbor] = Node(val = neighbor.val)
    #                 queue.append(neighbor)
    #             visited[n].neighbors.append(visited[neighbor])

    #     return visited[node]
