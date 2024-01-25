from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        queue = deque([root])
        while queue:
            n = len(queue)
            sum_ = 0
            for _ in range(n):
                node = queue.popleft()
                sum_ += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(sum_ / n)

        return ans
