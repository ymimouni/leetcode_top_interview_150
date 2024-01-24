from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compute_height(self, root: Optional[TreeNode]) -> int:
        depth = 0
        node = root
        while node:
            depth += 1
            node = node.left
        return depth

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = (left + right) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1

        return node is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = self.compute_height(root) - 1
        if d == 0:
            return 1

        left, right = 0, 2 ** d - 1
        while left <= right:
            pivot = (left + right) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return 2 ** d - 1 + left
