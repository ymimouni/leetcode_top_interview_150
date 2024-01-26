from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal i

            if not node:
                return None
            val = helper(node.left)
            if val is not None:
                return val
            if i == k:
                return node.val
            i += 1
            return helper(node.right)

        i = 1

        return helper(root)

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     stack = []

    #     cur = root
    #     i = 1
    #     while True:
    #         if cur is not None:
    #             stack.append(cur)
    #             cur = cur.left
    #         elif stack:
    #             cur = stack.pop()
    #             if i == k:
    #                 return cur.val
    #             i += 1
    #             cur = cur.right
    #         else:
    #             break

    #     return None

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def helper(node: Optional[TreeNode]) -> int:
#             nonlocal idx, stop, sol
#             if not node:
#                 return None

#             if not stop: helper(node.left)
#             if not stop and idx == k:
#                 sol = node.val
#                 stop = True
#                 return None
#             idx += 1
#             if not stop: helper(node.right)

#         idx = 1
#         stop = False
#         sol = 0
#         helper(root)
#         return sol
