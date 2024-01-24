class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                    # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right

                    # If there is no left child
            # then just go right.
            else:
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf

#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         ans = 0
#         stack = [(root, 0)]

#         while stack:
#             node, curr_sum = stack.pop()
#             if node:
#                 curr_sum = 10 * curr_sum + node.val
#                 if not node.left and not node.right:
#                     # If it's a leaf node, update ans.
#                     ans += curr_sum
#                 else:
#                     stack.append((node.left, curr_sum))
#                     stack.append((node.right, curr_sum))

#         return ans


#         ans = 0

#         def helper(node: TreeNode, path_sum: int) -> None:
#             nonlocal ans

#             path_sum = 10 * path_sum + node.val

#             if not node.left and not node.right:
#                 # If this is a leaf node.
#                 ans += path_sum
#                 return None
#             if node.left:
#                 # Visit the left subtree.
#                 helper(node.left, path_sum)
#             if node.right:
#                 # Visit the right subtree.
#                 helper(node.right, path_sum)

#         helper(root, 0)
#         return ans
