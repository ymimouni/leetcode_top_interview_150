from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def backtrack(start_r: int, start_c: int, length: int) -> "Node":
            if length == 1:
                return Node(val=grid[start_r][start_c], isLeaf=True)

            half_length = length // 2
            top_left = backtrack(start_r, start_c, half_length)
            top_right = backtrack(start_r, start_c + half_length, half_length)
            bottom_left = backtrack(start_r + half_length, start_c, half_length)
            bottom_right = backtrack(
                start_r + half_length, start_c + half_length, half_length
            )

            # If the four returned nodes are leaf nodes and have the same value.
            # Return a leaf node with the same value.
            if (
                top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
                and top_left.val == top_right.val
                and top_left.val == bottom_left.val
                and top_left.val == bottom_right.val
            ):
                return Node(val=top_left.val, isLeaf=True)

            return Node(
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right,
            )

        return backtrack(0, 0, len(grid))


# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
#         def same_value(start_r: int, start_c: int, length: int) -> bool:
#             for row in range(start_r, start_r + length):
#                 for col in range(start_c, start_c + length):
#                     if grid[row][col] != grid[start_r][start_c]:
#                         return False
#             return True

#         def backtrack(start_r, start_c, length):
#             if same_value(start_r, start_c, length):
#                 return Node(val=grid[start_r][start_c], isLeaf=True)
#             else:
#                 node = Node(isLeaf=False)
#                 half_length = length // 2
#                 node.topLeft = backtrack(start_r, start_c, half_length)
#                 node.topRight = backtrack(start_r, start_c + half_length, half_length)
#                 node.bottomLeft = backtrack(start_r + half_length, start_c, half_length)
#                 node.bottomRight = backtrack(start_r + half_length, start_c + half_length, half_length)

#                 return node

#         N = len(grid)
#         return backtrack(0, 0, N)
