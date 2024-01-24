from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root.left, root.right])

        while queue:
            t1, t2 = queue.popleft(), queue.popleft()
            if t1 is None and t2 is None:
                continue
            elif t1 is None or t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            queue.extend([t1.left, t2.right, t1.right, t2.left])

        return True

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     def helper(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    #         if n1 is None and n2 is None:
    #             return True
    #         elif n1 is None or n2 is None or n1.val != n2.val:
    #             return False
    #         else:
    #             return helper(n1.right, n2.left) and helper(n1.left, n2.right)

    #     return helper(root.left, root.right)
