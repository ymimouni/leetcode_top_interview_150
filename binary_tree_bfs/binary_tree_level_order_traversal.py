from collections import  deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> Optional[List[List[int]]]:
        if not root:
            return root

        ans = []
        queue = deque([root])
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            ans.append(level)

        return ans
