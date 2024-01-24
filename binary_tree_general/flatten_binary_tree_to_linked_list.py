from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        START, END = 1, 2

        stack = [(root, START)]

        tailnode = None
        while stack:
            node, status = stack.pop()

            if not node.left and not node.right:
                tailnode = node
                continue

            if status == START:
                if node.left:
                    stack.append((node, END))
                    stack.append((node.left, START))
                else:
                    stack.append((node.right, START))
            else:
                if tailnode:
                    tailnode.right = node.right
                    node.right = node.left
                    node.left = None

                stack.append((node.right, START))

        return root

    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
    #         if not node:
    #             return None

    #         if not node.left and not node.right:
    #             return node

    #         left_tail = helper(node.left)
    #         right_tail = helper(node.right)

    #         if left_tail:
    #             left_tail.right = node.right
    #             node.right = node.left
    #             node.left = None

    #         return right_tail if right_tail else left_tail

    #     helper(root)
    #     return root
