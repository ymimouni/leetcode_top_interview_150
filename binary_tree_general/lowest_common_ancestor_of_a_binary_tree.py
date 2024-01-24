class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Three flags to track the post-order traversal.

    # Indicates that we still need to traverse both left and right children.
    BOTH_PENDING = 2

    # Indicates that the child is done.
    LEFT_DONE = 1

    # Indicates that both children are already traversed.
    # We can remove the node from the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        # Init the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # Indicates that either p or q were found.
        one_node_found = False

        # Keep track of the index of the least common ancestor.
        LCA_index = -1

        # Post-order traversal of the tree.
        while stack:
            parent_node, parent_state = stack[-1]

            # If parent node is not done yet.
            if parent_state != Solution.BOTH_DONE:

                # If both children are pending.
                if parent_state == Solution.BOTH_PENDING:

                    # If the current node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If we have already found the other node.
                        if one_node_found:
                            return stack[LCA_index][0]
                        # Else, keep track of the index.
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1

                    # Both pending, traverse the left child first.
                    child_node = parent_node.left

                else:
                    # Traverse right child.
                    child_node = parent_node.right

                # Update the status of the parent node.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))

            else:
                # Node already done, remove it from the stack.

                # If LCA_index is equal to the length of the stack. Then decrease by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1

                stack.pop()

        return None

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # Stack for tree traversal.
#         stack = [root]

#         # Map to keep parent pointers.
#         parent = {root: None}

#         # Iterate until we find both p and q.
#         while p not in parent or q not in parent:
#             curr = stack.pop()

#             # While traversing the tree, keep saving the parents.
#             if curr.left:
#                 parent[curr.left] = curr
#                 stack.append(curr.left)

#             if curr.right:
#                 parent[curr.right] = curr
#                 stack.append(curr.right)

#         # Ancestors of p.
#         ancestors = set()

#         while p:
#             ancestors.add(p)
#             p = parent[p]

#         # The first ancestor of q which apperas in p's ancestors is the lowest common ancestor.
#         while q not in ancestors:
#             q = parent[q]

#         return q

#     def __init__(self):
#         self.ans = None

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         def recurse_tree(curr):
#             # If we reached the end, return False.
#             if not curr:
#                 return False

#             # Left recursion.
#             left = recurse_tree(curr.left)

#             # Right recursion.
#             right = recurse_tree(curr.right)

#             # If the current node is one of p or q.
#             mid = True if curr is p or curr is q else False

#             # If any two of the three flags become True.
#             if mid + left + right >= 2:
#                 self.ans = curr

#             # Return True if either of the three flags is True.
#             return left or mid or right

#         recurse_tree(root)
#         return self.ans
