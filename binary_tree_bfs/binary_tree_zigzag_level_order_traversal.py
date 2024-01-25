from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> Optional[List[List[int]]]:
        if not root:
            return root
        cur = deque([root])

        zig = True
        levels = []
        while cur:
            level = []
            next_ = deque()
            n = len(cur)
            for _ in range(n):
                if zig:
                    node = cur.popleft()
                else:
                    node = cur.pop()
                level.append(node.val)
                if zig:
                    if node.left: next_.append(node.left)
                    if node.right: next_.append(node.right)
                else:
                    if node.right: next_.appendleft(node.right)
                    if node.left: next_.appendleft(node.left)

            zig = False if zig else True
            levels.append(level)
            cur = next_

        return levels
