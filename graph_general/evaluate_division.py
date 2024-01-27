from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gid_weight = {}

        def find(node_id: int) -> (int, int):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1.0)

            group_id, node_weight = gid_weight[node_id]
            if node_id != group_id:
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = (new_group_id, node_weight * group_weight)

            return gid_weight[node_id]

        def union(divident: int, divisor: int, weight: float) -> None:
            divident_gid, divident_weight = find(divident)
            divisor_gid, divisor_weight = find(divisor)
            if divident_gid != divisor_gid:
                gid_weight[divident_gid] = (divisor_gid, divisor_weight * weight / divident_weight)

        # Step 1 = build union groups.
        for (divident, divisor), value in zip(equations, values):
            union(divident, divisor, value)

        results = []
        # Step 2 - Run the evaluation of each query.
        for (divident, divisor) in queries:
            if divident not in gid_weight or divisor not in gid_weight:
                ret = -1.0
            elif divident == divisor:
                ret = 1.0
            else:
                divident_gid, divident_weight = find(divident)
                divisor_gid, divisor_weight = find(divisor)
                if divident_gid != divisor_gid:
                    ret = -1.0
                else:
                    ret = divident_weight / divisor_weight
            results.append(ret)

        return results

    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     graph = defaultdict(defaultdict)

    #     def dfs(divident: int, divisor: int) -> Optional[int]:
    #         visited.add(divident)
    #         if divisor in graph[divident]:
    #             return graph[divident][divisor]

    #         for neighbor in graph[divident]:
    #             if neighbor not in visited:
    #                 result = dfs(neighbor, divisor)
    #                 if result:
    #                     return graph[divident][neighbor] * result

    #         return None

    #     # Step 1 - build the graph from the equations.
    #     for (divident, divisor), value in zip(equations, values):
    #         graph[divident][divisor] = value
    #         graph[divisor][divident] = 1 / value

    #     # Step 2 - evaluate each query using DFS
    #     results = []
    #     for divident, divisor in queries:
    #         if divident not in graph or divisor not in graph:
    #             results.append(-1.0)
    #         elif divident == divisor:
    #             results.append(1.0)
    #         else:
    #             visited = set()
    #             result = dfs(divident, divisor)
    #             results.append(result if result else -1.0)

    #     return results
